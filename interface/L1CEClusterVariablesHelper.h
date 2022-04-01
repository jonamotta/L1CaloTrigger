#ifndef L1Trigger_L1CaloTrigger_L1CEClusterVariablesHelper_h
#define L1Trigger_L1CaloTrigger_L1CEClusterVariablesHelper_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/L1THGCal/interface/HGCalMulticluster.h"
#include <vector>
#include <cmath>
#include <math.h>

class L1CEClusterVariablesHelper {
private:

public:
    float getClusterVariable(std::string variable, const l1t::HGCalMulticluster* cluster);
};

#endif