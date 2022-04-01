#include "L1Trigger/L1CaloTrigger/interface/L1TauCEpuRejector.h"

L1TauCEpuRejector::L1TauCEpuRejector(const std::string& pathToPUBDT){
    PUBDT_->initialize("!Color:Silent:!Error",
                       "BDT::BDTG",
                       pathToPUBDT,
                       PUfeatures_,
                       spectators_,
                       false,
                       false);
}

float L1TauCEpuRejector::PUrej(const l1t::HGCalMulticluster* cl3d, float c3_factor){
    std::map<std::string, float> inputs;
    for (unsigned i = 0; i < PUfeatures_.size(); i++) {
        if (PUfeatures_[i] == "cl3d_c3") { inputs[PUfeatures_[i]] = c3_factor; }
        else { inputs[PUfeatures_[i]] = varsHelper_.getClusterVariable(PUfeatures_[i], cl3d); }
    }

    return PUBDT_->evaluate(inputs);;
}