#ifndef L1Trigger_L1CaloTrigger_L1TauCEisoRejector_h
#define L1Trigger_L1CaloTrigger_L1TauCEisoRejector_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/L1THGCal/interface/HGCalMulticluster.h"
#include "CommonTools/MVAUtils/interface/TMVAEvaluator.h"
#include "L1Trigger/L1CaloTrigger/interface/L1CEClusterVariablesHelper.h"
#include <vector>
#include <cmath>
#include <math.h>

class L1TauCEisoRejector {
public:
    explicit L1TauCEisoRejector(const std::string& pathToISOBDT);

    float ISOrej(const l1t::HGCalMulticluster* cl3d, float cl3d_pt_c3, int NclIso, float tower_etSgn1, float tower_etSgn2, float tower_etIso);

private:
    L1CEClusterVariablesHelper varsHelper_;

    // PU REJECTION VARIABLES
    std::unique_ptr<TMVAEvaluator> ISOBDT_ = std::unique_ptr<TMVAEvaluator>(new TMVAEvaluator);
    const std::vector<std::string> ISOfeatures_ { "cl3d_pt_tr", "cl3d_abseta", "cl3d_spptot", "cl3d_srrtot", "cl3d_srrmean", "cl3d_hoe", "cl3d_meanz", "cl3d_NclIso_dR4", "tower_etSgn_dRsgn1", "tower_etSgn_dRsgn2", "tower_etIso_dRsgn1_dRiso3" };
    const std::vector<std::string> spectators_ = {};

};

#endif