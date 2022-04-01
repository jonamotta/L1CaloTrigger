#include "L1Trigger/L1CaloTrigger/interface/L1TauCEisoRejector.h"

L1TauCEisoRejector::L1TauCEisoRejector(const std::string& pathToISOBDT){
    ISOBDT_->initialize("!Color:Silent:!Error",
                       "BDT::BDTG",
                       pathToISOBDT,
                       ISOfeatures_,
                       spectators_,
                       false,
                       false);
}

float L1TauCEisoRejector::ISOrej(const l1t::HGCalMulticluster* cl3d, float cl3d_pt_c3, int NclIso, float tower_etSgn1, float tower_etSgn2, float tower_etIso){
    std::map<std::string, float> inputs;
    for (unsigned i = 0; i < ISOfeatures_.size(); i++) {
        if      (ISOfeatures_[i] == "cl3d_pt_tr") { inputs[ISOfeatures_[i]] = cl3d_pt_c3; }
        else if (ISOfeatures_[i] == "cl3d_NclIso_dR4") { inputs[ISOfeatures_[i]] = NclIso; }
        else if (ISOfeatures_[i] == "tower_etSgn_dRsgn1") { inputs[ISOfeatures_[i]] = tower_etSgn1; }
        else if (ISOfeatures_[i] == "tower_etSgn_dRsgn2") { inputs[ISOfeatures_[i]] = tower_etSgn2; }
        else if (ISOfeatures_[i] == "tower_etIso_dRsgn1_dRiso3") { inputs[ISOfeatures_[i]] = tower_etIso; }
        else { inputs[ISOfeatures_[i]] = varsHelper_.getClusterVariable(ISOfeatures_[i], cl3d); }
    }

    return ISOBDT_->evaluate(inputs);;
}