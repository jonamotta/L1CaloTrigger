#include "L1Trigger/L1CaloTrigger/interface/L1CEClusterVariablesHelper.h"

float L1CEClusterVariablesHelper::getClusterVariable(std::string variable, const l1t::HGCalMulticluster* cluster){
    if      (variable == "cl3d_showerlength")     { return cluster->showerLength(); }
    else if (variable == "cl3d_coreshowerlength") { return cluster->coreShowerLength(); }
    else if (variable == "cl3d_firstlayer")       { return cluster->firstLayer(); }
    else if (variable == "cl3d_maxlayer")         { return cluster->maxLayer(); }
    else if (variable == "cl3d_seetot")           { return cluster->sigmaEtaEtaTot(); }
    else if (variable == "cl3d_seemax")           { return cluster->sigmaEtaEtaMax(); }
    else if (variable == "cl3d_spptot")           { return cluster->sigmaPhiPhiTot(); }
    else if (variable == "cl3d_sppmax")           { return cluster->sigmaPhiPhiMax(); }
    else if (variable == "cl3d_szz")              { return cluster->sigmaZZ(); }
    else if (variable == "cl3d_srrtot")           { return cluster->sigmaRRTot(); }
    else if (variable == "cl3d_srrmax")           { return cluster->sigmaRRMax(); }
    else if (variable == "cl3d_srrmean")          { return cluster->sigmaRRMean(); }
    //else if (variable == "cl3d_hoe")              { return cluster->hOverE(); }
    else if (variable == "cl3d_meanz")            { return abs(cluster->zBarycenter()); }
    else if (variable == "cl3d_eta")              { return cluster->eta(); }
    else if (variable == "cl3d_abseta")           { return abs(cluster->eta()); }
    else if (variable == "cl3d_phi")              { return cluster->phi(); }
    else if (variable == "cl3d_pt")               { return cluster->pt(); }
    else                                          { return 0.; }
}