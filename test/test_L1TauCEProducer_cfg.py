import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('L1REPR',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# initialize MessageLogger and output report
process.MessageLogger = cms.Service("MessageLogger",
       destinations   = cms.untracked.vstring('tmp_detailedInfo' , 'tmp_critical', 'tmp_cout', 'tmp_cerr'),
       tmp_detailedInfo = cms.untracked.PSet(threshold = cms.untracked.string('ERROR') ),
       tmp_critical     = cms.untracked.PSet(threshold = cms.untracked.string('INFO') ),
       tmp_cout         = cms.untracked.PSet(threshold = cms.untracked.string('DEBUG') ),
       tmp_cerr         = cms.untracked.PSet(threshold  = cms.untracked.string('WARNING') )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/1340000/AD71756A-C44A-AC4F-97E2-9473DD8406B9.root', 
        #'/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/039D74B4-0290-A542-A2F2-BB33E8AB3320.root'
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/0450E331-AC92-494A-9929-7F7C108BE43E.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/0A2078B7-4525-BD40-8F24-61C41DED1CEA.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/0DAECEA0-1A27-334A-97F2-A8EB0410ABA9.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/0E384C52-7890-6C4D-A6E3-46E3832DBFE5.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/0FEC4A54-6F28-1F43-9782-476602184E4A.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/119982F8-9051-794A-A6DA-278D3B2B9D3E.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/16B2ABDB-3748-5A4D-B3C6-910C9095A562.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/1BBF42F2-E760-2B49-BF66-ACD8EC2EE4DC.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/1C151EC3-75B0-8649-844C-84AABE50578F.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/24C68351-EF3D-4A48-99DA-AFEE1B41FCCD.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/49A3C89E-AE65-6F49-95E7-79B8E7CE060E.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/4F83AC52-30FD-8441-8D35-0D1D88453A06.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/50EEACF6-C170-8E4A-A53D-CBB81C6779D8.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/539486C5-24B4-AE4C-A337-B95F5578EE66.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/5676958E-7CF7-C243-AF3E-2F56BD1C8828.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/5CCAF9A1-27F5-5F44-A9C1-7854DD337625.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/5EC5C821-0181-1840-B98D-E7662EB955E2.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/6219DD89-F8E8-5843-834B-02A167A28769.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/6915B50A-3E6B-3148-927E-0471CCAC10C3.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/73C2C7EC-559A-B14C-A98E-C657603FEC47.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/77BA80E8-DE11-CE48-84FD-A090C0BBBA0B.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/791A1CB1-8785-7241-A2CD-D669AEDC054F.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/7CE29609-1D6D-5942-9CC5-328A380F43E7.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/80897EF0-EF4E-7545-A3C6-73171C0A1695.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/8DA19CAA-D662-2049-A7EF-BED35B35C9C9.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/90706D9F-4432-9D4D-8FB8-A4CB61065970.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/9C510A15-FF62-564F-AD99-48747E61A587.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/ADD0E235-1AFF-1A4F-B10C-33047E29814E.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/ADE67361-D3BD-794A-A4D3-54B541F5C4D3.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/AF58977A-E933-B646-B275-B59DA6E78A9F.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/B662B6F4-3085-BE4F-91B2-72ABE176AA9A.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/B6F96524-155E-5440-AF87-E079CE848B0B.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/B7922FFB-2367-F643-97BA-28744D23787C.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/B7A7C0B4-8CCE-9140-B1FC-B97DAC57FA94.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/BFA6C6A3-424D-804C-B558-3F034D8B5A22.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/C0C9DE3D-BB67-5C4D-825F-7FA4FB0B0269.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/C2319EF3-0E12-FA41-90A2-5BD81BC56D10.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/C3A66F2C-FC20-3F46-B96E-4853AF81F7E5.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/C577E370-3E7E-5649-925D-99E4602C7540.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/C5A99CE8-D915-6343-A4EC-DD07FFC80AB6.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/C8887A96-EEE8-7E4C-857D-2859AC0574EA.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/D011BFE0-2AED-F949-BB1C-B551A655DBAA.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/D2AC181D-0C92-564C-B02E-861928A444DE.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/D5A858F2-C84C-F545-B056-47CC7E5BB4E2.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/D612B562-5B1B-544D-A62D-01364BBC6307.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/DA84877A-4E30-BC4A-9D9C-6C0616005C34.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/DC10673D-0340-0E47-B7A8-F3C7B14FD46A.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/E2EAA734-0DBB-644F-BFB0-856F9517A8DE.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/EA1BCA68-90DE-424E-A68B-07CC825E7C07.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/EDDCA856-5DC9-7B4F-BAEB-090989CDEEB0.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/F06D0712-BCDA-7449-8EEE-871867A833E6.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/F3326A04-25D2-9240-B509-7038CCEC62D3.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/F984F60E-245A-C143-9ACC-34A8C9B3A6F3.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2530000/FF919B39-19E7-5A4D-AD38-1E10408E4458.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/56B50084-13D3-AF46-A630-C5DB0F30F236.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/A9560570-6CCF-1849-8FC2-4AF72A4401DC.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/AFA110B0-A805-9443-89B3-B0B231F5E39C.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/B03F623E-16AE-154B-9D91-AA40B92BFEB2.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/CAB5414F-B823-E544-B44E-FE914A94D060.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/E52FB61A-9646-8440-9A87-2FF41D7AC849.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/260000/E746B808-F57A-534B-AD53-24AD6226774F.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/14F0012A-C9AB-2F43-93F5-9110E993789E.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/1BEC9FF6-10DB-5A4F-8AD4-A5751C2CF7F7.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/2261173F-58A2-6F40-8D75-777B0C817B81.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/2EF7CF83-9019-BA47-BFD5-9112F2D1ED9E.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/3D481082-FC84-674F-B817-67DCD160A7F2.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/5E3EF3C6-4784-5E48-9BD5-3DDCB248BE54.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/6B4AF252-6D41-2A45-AD9F-5E61075773E6.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/A9D7B8CF-042C-BD46-AF29-5F9634ED00FF.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/B74B734F-9D94-BD48-8209-604426415BA5.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/E96FFA64-1819-444C-9C7C-7998803D0106.root', 
        # '/store/mc/Phase2HLTTDRSummer20L1T/MinBias_TuneCP5_14TeV-pythia8/FEVT/PU200_111X_mcRun4_realistic_T15_v1-v2/2610000/EB65D1E9-073B-1C49-8F18-41D7A7ED52F1.root'
    ),
    secondaryFileNames = cms.untracked.vstring(),
    inputCommands = cms.untracked.vstring(
                          "keep *",
                          "drop l1tPFCandidates_*_*_*"
    )
)


# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('test nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('tmp.root')
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# load tau endcap producer
process.load('L1Trigger.L1CaloTrigger.L1TauCEProducer_cff')

# Path and EndPath definitions
#process.raw2digi_step = cms.Path(process.RawToDigi)
process.hgcL1TauTrigger_step = cms.Path(process.L1TauCEProducerTask)
#process.endjob_step = cms.EndPath(process.endOfProcess)
process.out_step = cms.EndPath(process.out)

# Schedule definition
#process.schedule = cms.Schedule(process.raw2digi_step, process.hgcL1TauTrigger_step, process.endjob_step, process.out_step)
process.schedule = cms.Schedule(process.hgcL1TauTrigger_step, process.out_step)

# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion