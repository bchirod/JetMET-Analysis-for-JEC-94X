from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'test_QCD_NoPU_JRA_90'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'run_JRA_hlt_cfg.py'
#config.JobType.inputFiles    = ['PFCalibration_HLT_2017_25ns_Summer17_V1.db']
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.inputDBS = 'phys03'

#Change it to your dataset
config.Data.inputDataset = '/QCD_Pt-15to3000_TuneCP5_Flat_13TeV_pythia8/bchitrod-QCD_NoPU_10X_JEC_ALL-6061c8cf151e4bbba4918201877e8b6e/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 90
#config.Data.totalUnits = 10

#Change it to your directory
config.Data.outLFNDirBase = '/store/user/bchitrod/10X/QCD_NoPU_JRA_90'

#config.Data.useParent = True 
#config.Data.lumiMask = '/afs/cern.ch/user/m/mdjordje/public/2017JSON/Cert_13TeV_2017_HCAL_DCS_GOOD.txt'
config.JobType.maxMemoryMB = 4000

# This string is used to construct the output dataset name
#config.Data.publishDataName = 'CRAB3-tutorial'

#config.Data.publication = True
#config.Data.publishDBS = 'phys03'
#config.Data.outputDatasetTag = 'QCD_NoPU_92X_JEC_5'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_IN_TIFR'
#config.Site.whitelist = ["T2_CH_CERN"]
