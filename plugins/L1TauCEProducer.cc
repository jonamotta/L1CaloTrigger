#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/L1THGCal/interface/HGCalMulticluster.h"
#include "DataFormats/L1THGCal/interface/HGCalTower.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/L1Trigger/interface/Tau.h"
#include "L1Trigger/L1CaloTrigger/interface/L1TauCECalibrator.h"
#include "L1Trigger/L1CaloTrigger/interface/L1TauCEpuRejector.h"
#include "L1Trigger/L1CaloTrigger/interface/L1TauCEisoRejector.h"
#include "DataFormats/Math/interface/deltaPhi.h"

class L1TauCEProducer : public edm::stream::EDProducer<> {
public:
    explicit L1TauCEProducer(const edm::ParameterSet &);

private:
    void produce(edm::Event &, const edm::EventSetup &) override;

    edm::EDGetToken multiclusters_token_;
    edm::EDGetToken hgcalTowers_token_;
    
    std::string pathToC2BDT = "L1Trigger/L1CaloTrigger/data/C2model_nonRscld_booster.onnx";
    std::string pathToC2dummy = "L1Trigger/L1CaloTrigger/data/GBDT_default.onnx";
    L1TauCECalibrator calibrator_;
    
    std::string pathToPUBDT = "L1Trigger/L1CaloTrigger/data/PUmodel_nonRscld.xml";
    L1TauCEpuRejector puRejector_;
    //float PUWP = 0.008968670945614576;
    //float PUWP = -0.9910313291;
    float PUWP = -0.008968430482;

    std::string pathToISOBDT = "L1Trigger/L1CaloTrigger/data/ISOmodel_nonRscld.xml";
    L1TauCEisoRejector isoRejector_;
    //float ISOWP = 0.11654538989067077;
    //float ISOWP = -0.8834546101;
    float ISOWP = -0.7669092202;

    // sgn and iso cones
    float dRcl3d_ = 0.4;
    float dRsgn1_ = 0.1;
    float dRsgn2_ = 0.2;
    float dRiso_  = 0.3;
};

L1TauCEProducer::L1TauCEProducer(const edm::ParameterSet &iConfig) 
    : multiclusters_token_(consumes<l1t::HGCalMulticlusterBxCollection>(iConfig.getParameter<edm::InputTag>("Multiclusters"))),
        hgcalTowers_token_(consumes<l1t::HGCalTowerBxCollection>(iConfig.getParameter<edm::InputTag>("HgcalTowers"))),
        calibrator_(pathToC2BDT),
        puRejector_(pathToPUBDT),
        isoRejector_(pathToISOBDT) {
    produces<BXVector<l1t::Tau>>("L1TauCollectionBXV");
}

void L1TauCEProducer::produce(edm::Event &iEvent, const edm::EventSetup &iSetup) {
    float minPt_ = 4;
    float minEta_ = 1.6;
    float maxEta_ = 2.9;

    std::unique_ptr<BXVector<l1t::Tau>> l1TauBxCollection(new l1t::TauBxCollection);

    // retrieve clusters 3D
    edm::Handle<l1t::HGCalMulticlusterBxCollection> multiclusters_h;
    iEvent.getByToken(multiclusters_token_, multiclusters_h);
    const l1t::HGCalMulticlusterBxCollection &multiclusters = *multiclusters_h;

    // retrieve towers
    edm::Handle<l1t::HGCalTowerBxCollection> hgcalTowers_h;
    iEvent.getByToken(hgcalTowers_token_, hgcalTowers_h);
    const l1t::HGCalTowerBxCollection &hgcalTowers = *hgcalTowers_h; // = (*hgcalTowers_h.product()); ???

    std::vector< std::pair<const l1t::HGCalMulticluster*, float> > selected_multiclusters;

    int i = 0; //DEBUG
    int j = 0; //DEBUG
    // here we loop on the TPs
    for (auto cl3d = multiclusters.begin(0); cl3d != multiclusters.end(0); cl3d++) {
        i += 1; //DEBUG
        if (cl3d->pt() <= minPt_) { continue; }
        if ((abs(cl3d->eta()) >= maxEta_) || (abs(cl3d->eta()) <= minEta_)) { continue; }

        j += 1; //DEBUG

        // do calibration
        float c1_factor = calibrator_.C1calib(abs(cl3d->eta()));
        float c2_factor = calibrator_.C2calib_onnx(&(*cl3d), pathToC2BDT);
        float c3_factor = calibrator_.C3calib( abs((cl3d->pt()+c1_factor)*c2_factor) );

        // do PU rejection
        //float score = puRejector_.PUrej(&(*cl3d), c3_factor_skl);
        //if (score < PUWP) { continue; }

        // store selected TPs
        selected_multiclusters.push_back(std::pair(&(*cl3d), (cl3d->pt()-c1_factor)*c2_factor/c3_factor));
    }

    std::cout << "TOT CL3Ds = " << i << std::endl; //DEBUG
    std::cout << "ETA/PT pass CL3Ds = " << j << std::endl; //DEBUG
    std::cout << "SEL CL3Ds = " << selected_multiclusters.size() << std::endl; //DEBUG

    // ISO features to be computed
    int NclIso;
    float tower_etSgn1;
    float tower_etSgn2;
    float tower_etIso;

    int h = 0; //DEBUG
    // here we loop on the selected TPs to calculate ISO features
    for (long unsigned int i = 0; i < selected_multiclusters.size(); i++) {
        auto cl3d1 = selected_multiclusters[i].first;
        float cl3d1_pt_c3 = selected_multiclusters[i].second;

        if (cl3d1->pt() < 10) { continue; }

        // initialize ISO variables
        NclIso = 0;
        tower_etSgn1 = 0.0;
        tower_etSgn2 = 0.0;
        tower_etIso = 0.0;

        // loop over the selected TPs to calculate TPs ISO features
        for (long unsigned int j = 0; j < selected_multiclusters.size(); j++) {
            auto cl3d2 = selected_multiclusters[j].first;

            if (cl3d1->eta() == cl3d2->eta()) { continue; } // skip double counting
            float dR12 = sqrt( pow((cl3d1->eta() - cl3d2->eta()),2) + pow(reco::deltaPhi(cl3d1->phi(), cl3d2->phi()),2) );
            if (dR12 < dRcl3d_) { NclIso += 1; }
        }

        // loop over the Towers to calculate TPs ISO features
        for (auto tower = hgcalTowers.begin(0); tower != hgcalTowers.end(0); tower++) {
            if (std::abs(tower->eta())<1.5 || std::abs(tower->eta())>3.0) { continue; }
            float dRct = sqrt( pow((cl3d1->eta() - tower->eta()),2) + pow(reco::deltaPhi(cl3d1->phi(), tower->phi()),2) );
            if (dRct < dRsgn1_)                  { tower_etSgn1 += tower->etEm()+tower->etHad(); }
            if (dRct < dRsgn2_)                  { tower_etSgn2 += tower->etEm()+tower->etHad(); }
            if (dRct > dRsgn1_ && dRct < dRiso_) { tower_etIso += tower->etEm()+tower->etHad(); }
        }

        // do ISO rejection
        //float score = isoRejector_.ISOrej(cl3d1, cl3d1_pt_c3, NclIso, tower_etSgn1, tower_etSgn2, tower_etIso);
        //if (score < ISOWP) { continue; }

        h += 1; //DEBUG

        reco::Candidate::PolarLorentzVector tlv_tau(cl3d1_pt_c3, cl3d1->eta(), cl3d1->phi(), 0); // should mass be 0.0 or tau_mass?
        l1t::Tau l1Tau = l1t::Tau(tlv_tau);

        // store Tau candidates
        l1TauBxCollection->push_back(0, l1Tau); // is bx always 0 correct?
    }

    // store the Tau candidates per iEvent
    iEvent.put(std::move(l1TauBxCollection), "L1TauCollectionBXV");

    std::cout << "" << std::endl; //DEBUG
    std::cout << "TOT CL3Ds = " << i << std::endl; //DEBUG
    std::cout << "SEL CL3Ds = " << h << std::endl; //DEBUG
}

DEFINE_FWK_MODULE(L1TauCEProducer);