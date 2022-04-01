import FWCore.ParameterSet.Config as cms

L1TauCEProducer = cms.EDProducer("L1TauCEProducer",
                                 Multiclusters=cms.InputTag('hgcalBackEndLayer2Producer:HGCalBackendLayer2Processor3DClustering'),
                                 HgcalTowers=cms.InputTag("hgcalTowerProducer:HGCalTowerProcessor"))
