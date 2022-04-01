#ifndef L1Trigger_L1CaloTrigger_L1TauCEpuRejector_h
#define L1Trigger_L1CaloTrigger_L1TauCEpuRejector_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/L1THGCal/interface/HGCalMulticluster.h"
#include "CommonTools/MVAUtils/interface/TMVAEvaluator.h"
#include "L1Trigger/L1CaloTrigger/interface/L1CEClusterVariablesHelper.h"
#include <vector>
#include <cmath>
#include <math.h>

class L1TauCEpuRejector {
public:
    explicit L1TauCEpuRejector(const std::string& pathToPUBDT);

    float PUrej(const l1t::HGCalMulticluster* cl3d, float c3_factor);

private:
    L1CEClusterVariablesHelper varsHelper_;

    // PU REJECTION VARIABLES
    std::unique_ptr<TMVAEvaluator> PUBDT_ = std::unique_ptr<TMVAEvaluator>(new TMVAEvaluator);
    const std::vector<std::string> PUfeatures_ { "cl3d_c3", "cl3d_coreshowerlength", "cl3d_srrtot", "cl3d_srrmean", "cl3d_hoe", "cl3d_meanz" };
    const std::vector<std::string> spectators_ = {};

};

#endif