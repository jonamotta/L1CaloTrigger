#include "L1Trigger/L1CaloTrigger/interface/L1TauCECalibrator.h"

L1TauCECalibrator::L1TauCECalibrator(const std::string& pathToC2BDT){
    // // add input variables
    // for (std::vector<std::string>::const_iterator it = C2features_.begin(); it != C2features_.end(); ++it) {
    //   variables.insert(std::make_pair(*it, std::make_pair(it - C2features_.begin(), 0.)));
    //   C2BDT_->AddVariable(it->c_str(), &(variables.at(*it).second));
    // }

    // // book MVA method
    // C2BDT_->BookMVA("BDT::BDT", pathToC2BDT);
}

float L1TauCECalibrator::C1calib(const float& eta){
    return z_ + m_ * fabs(eta);
}

// float L1TauCECalibrator::C2calib(const l1t::HGCalMulticluster* cl3d){
//     // TMVA::Reader is not thread safe
//     std::lock_guard<std::mutex> lock(m_mutex);

//     // retrieve inputs
//     std::map<std::string, float> inputs;
//     for (unsigned i = 0; i < C2features_.size(); i++) {
//         inputs[C2features_[i]] = varsHelper_.getClusterVariable(C2features_[i], cl3d);
//     }

//     // set the input variable values
//     for (auto it = variables.begin(); it != variables.end(); ++it) {
//         it->second.second = inputs.at(it->first);
//     }

//     return (C2BDT_->EvaluateRegression("BDT::BDT"))[0];
// }

float L1TauCECalibrator::C2calib_onnx(const l1t::HGCalMulticluster* cl3d, const std::string pathToC2ONNX){
    std::cout << "before problematic point" << std::endl;
    // setup ONNX runtime
    cms::Ort::ONNXRuntime runtime(pathToC2ONNX);
    std::cout << "past problematic point" << std::endl;

    // retrieve inputs
    std::vector<float> inputs;
    for (unsigned i = 0; i < C2features_onnx_.size(); i++) {
        inputs.push_back(varsHelper_.getClusterVariable(C2features_onnx_[i], cl3d));
    }


    std::vector<std::string> input_names;
    input_names.push_back("feature_input");

    const std::vector<std::vector<int64_t>>& input_shapes = {};

    cms::Ort::FloatArrays ortinput;
    ortinput.push_back(inputs);

    std::vector<std::string> ortoutput_names;
    ortoutput_names = runtime.getOutputNames();

    std::cout << "here" <<endl; //DEBUG
    cms::Ort::FloatArrays ortoutput = runtime.run(input_names, ortinput, input_shapes, ortoutput_names, 1);
    std::cout << "here" <<endl; //DEBUG
    float score = ortoutput[0][0];
    std::cout << "here" <<endl; //DEBUG

    return score;
}


float L1TauCECalibrator::C3calib(const float& pt_c2){
    float log1 = pow(log(pt_c2), 1);
    float log2 = pow(log(pt_c2), 2);
    float log3 = pow(log(pt_c2), 3);
    float log4 = pow(log(pt_c2), 4);

    return k0_ + k1_*log1 + k2_*log2 + k3_*log3 + k4_*log4;
}