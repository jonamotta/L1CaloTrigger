# L1CaloTrigger

This repository contains the personal developments of the Phase-2 HGCAL CaloTau L1 Emulator.

The branch for-CMSSW_12_1_7 contains the first emulator built for an older release of CMSSW which now is not in use anymore.

The branch for-CMSSW_12_3_0_pre4 contains the updated emulator for the current CMSSW release.

For the current release, the installation instructions are:
```bash
cmsrel CMSSW_12_3_0_pre4
cd CMSSW_12_3_0_pre4/src
cmsenv
git cms-init
git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v3.4.20
git cms-addpkg L1Trigger/L1TMuon
git clone -u official-cmssw:phase2-l1t-integration-1230pre4 https://github.com/cms-l1t-offline/L1Trigger-L1TMuon.git L1Trigger/L1TMuon/data
scram b -j 12
```
then this repo can be cloned to substitute `CMSSW_12_3_0_pre4/src/L1Trigger/L1CaloTrigger`
