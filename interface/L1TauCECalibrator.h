#ifndef L1Trigger_L1CaloTrigger_L1TauCECalibrator_h
#define L1Trigger_L1CaloTrigger_L1TauCECalibrator_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/L1THGCal/interface/HGCalMulticluster.h"
#include "CommonTools/MVAUtils/interface/TMVAEvaluator.h"
#include "PhysicsTools/ONNXRuntime/interface/ONNXRuntime.h"
#include "L1Trigger/L1CaloTrigger/interface/L1CEClusterVariablesHelper.h"
#include <vector>
#include <cmath>
#include <math.h>

class L1TauCECalibrator {
public:
    explicit L1TauCECalibrator(const std::string& pathToC2BDT);

    float C1calib(const float& eta);
    // float C2calib(const l1t::HGCalMulticluster* cl3d);
    float C3calib(const float& pt);

    float C2calib_onnx(const l1t::HGCalMulticluster* cl3d, const std::string pathToC2ONNX);

private:
    L1CEClusterVariablesHelper varsHelper_;

    // C1 VARIABLES
    const float m_ = -13.279065;
    const float z_ = 46.173668;

    // C2 VARIABLES
    // mutable std::mutex m_mutex;
    // CMS_THREAD_GUARD(m_mutex) TMVA::Reader* C2BDT_ = new TMVA::Reader("!Color:Silent:!Error");
    // CMS_THREAD_GUARD(m_mutex) mutable std::map<std::string, std::pair<size_t, float>> variables;
    // const std::vector<std::string> C2features_ { "cl3d_abseta", "cl3d_coreshowerlength", "cl3d_meanz", "cl3d_showerlength", "cl3d_spptot", "cl3d_srrmean" };

    const std::vector<std::string> C2features_onnx_ { "cl3d_showerlength", "cl3d_coreshowerlength", "cl3d_abseta", "cl3d_spptot", "cl3d_srrmean", "cl3d_meanz" };
    const std::string pathToC2ONNX_ = "";


    // C3 VARIABLES
    const float k0_ =  82.61298096343806;
    const float k1_ =  -72.57047753753933;
    const float k2_ =  24.003302612116766;
    const float k3_ =  -3.4926634131095224;
    const float k4_ =  0.18802688117558475;

};

#endif