import FWCore.ParameterSet.Config as cms

process = cms.Process("JRA")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/group/phys_jetmet/bchitrod/11X_Step3_QCD_NoPU/QCD_Pt_15to3000_Flat_14TeV_NoPU/QCD_Pt-15to3000_TuneCP5_Flat_14TeV-pythia8/crab_11X_Step3QCD_Pt_15to3000_Flat_14TeV_NoPU/200614_234154/0000/QCD_Pt_15to3000_Flat_14TeV_NoPU_99.root')
)
process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

process.ak4caloHLTJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4caloHLTGenPtEta"),
    srcRec = cms.InputTag("ak4caloHLTPtEta")
)


process.ak4caloHLTJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4caloHLTPtEtaUncor"),
    srcRec = cms.InputTag("ak4caloHLTPtEta")
)


process.ak4pfHLTJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfHLTGenPtEta"),
    srcRec = cms.InputTag("ak4pfHLTPtEta")
)


process.ak4pfHLTJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak4pfHLTPtEtaUncor"),
    srcRec = cms.InputTag("ak4pfHLTPtEta")
)


process.ak8caloHLTJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak8caloHLTGenPtEta"),
    srcRec = cms.InputTag("ak8caloHLTPtEta")
)


process.ak8caloHLTJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak8caloHLTPtEtaUncor"),
    srcRec = cms.InputTag("ak8caloHLTPtEta")
)


process.ak8pfHLTJetToRef = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak8pfHLTGenPtEta"),
    srcRec = cms.InputTag("ak8pfHLTPtEta")
)


process.ak8pfHLTJetToUncorJet = cms.EDProducer("MatchRecToGen",
    srcGen = cms.InputTag("ak8pfHLTPtEtaUncor"),
    srcRec = cms.InputTag("ak8pfHLTPtEta")
)


process.pfNoPileUpJME = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpJME"),
    verbose = cms.untracked.bool(False)
)


process.pfPileUpJME = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("goodOfflinePrimaryVertices"),
    checkClosestZVertex = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.ak4caloHLTGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4GenJets")
)


process.ak4caloHLTPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK4CaloJets")
)


process.ak4caloHLTPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK4CaloJets")
)


process.ak4pfHLTGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak4GenJets")
)


process.ak4pfHLTPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK4PFJets")
)


process.ak4pfHLTPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK4PFJets")
)


process.ak8caloHLTGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak8GenJets")
)


process.ak8caloHLTPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK8CaloJets")
)


process.ak8caloHLTPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK8CaloJets")
)


process.ak8pfHLTGenPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("ak8GenJets")
)


process.ak8pfHLTPtEta = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK8PFJets")
)


process.ak8pfHLTPtEtaUncor = cms.EDFilter("EtaPtMinCandViewRefSelector",
    etaMax = cms.double(5.5),
    etaMin = cms.double(-5.5),
    ptMin = cms.double(1.0),
    src = cms.InputTag("hltAK8PFJets")
)


process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
    cut = cms.string('!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.ak4caloHLT = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.25),
    deltaRPartonMax = cms.double(0.25),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(True),
    doHLT = cms.bool(True),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcJetToUncorJetMap = cms.InputTag("ak4caloHLTJetToUncorJet","rec2gen"),
    srcJetUnMatch = cms.InputTag("ak4caloHLTJetToRef","unmaprec"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak4caloHLTGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak4caloHLTJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag("hltFixedGridRhoFastjetAllCalo"),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("hltPixelVertices")
)


process.ak4pfHLT = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.25),
    deltaRPartonMax = cms.double(0.25),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(True),
    doHLT = cms.bool(True),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcJetToUncorJetMap = cms.InputTag("ak4pfHLTJetToUncorJet","rec2gen"),
    srcJetUnMatch = cms.InputTag("ak4pfHLTJetToRef","unmaprec"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak4pfHLTGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak4pfHLTJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag("hltFixedGridRhoFastjetAll"),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("hltPixelVertices")
)


process.ak8caloHLT = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.25),
    deltaRPartonMax = cms.double(0.25),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(True),
    doHLT = cms.bool(True),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcJetToUncorJetMap = cms.InputTag("ak8caloHLTJetToUncorJet","rec2gen"),
    srcJetUnMatch = cms.InputTag("ak8caloHLTJetToRef","unmaprec"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak8caloHLTGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak8caloHLTJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo"),
    srcRhoHLT = cms.InputTag("hltFixedGridRhoFastjetAllCalo"),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("hltPixelVertices")
)


process.ak8pfHLT = cms.EDAnalyzer("JetResponseAnalyzer",
    deltaRMax = cms.double(0.25),
    deltaRPartonMax = cms.double(0.25),
    doComposition = cms.bool(True),
    doFlavor = cms.bool(True),
    doHLT = cms.bool(True),
    doJetPt = cms.bool(True),
    doRefPt = cms.bool(True),
    jecLabel = cms.string(''),
    nRefMax = cms.uint32(0),
    saveCandidates = cms.bool(False),
    srcJetToUncorJetMap = cms.InputTag("ak8pfHLTJetToUncorJet","rec2gen"),
    srcJetUnMatch = cms.InputTag("ak8pfHLTJetToRef","unmaprec"),
    srcPFCandidates = cms.InputTag(""),
    srcRef = cms.InputTag("ak8pfHLTGenPtEta"),
    srcRefToJetMap = cms.InputTag("ak8pfHLTJetToRef","gen2rec"),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll"),
    srcRhoHLT = cms.InputTag("hltFixedGridRhoFastjetAll"),
    srcRhos = cms.InputTag(""),
    srcVtx = cms.InputTag("hltPixelVertices")
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(5000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(False),
    fileName = cms.string('JRA.root')
)


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('.'),
        connectionRetrialPeriod = cms.untracked.int32(10),
        connectionRetrialTimeOut = cms.untracked.int32(60),
        connectionTimeOut = cms.untracked.int32(0),
        enableConnectionSharing = cms.untracked.bool(True),
        enablePoolAutomaticCleanUp = cms.untracked.bool(False),
        enableReadOnlySessionOnUpdateConnection = cms.untracked.bool(False),
        idleConnectionCleanupPeriod = cms.untracked.int32(10),
        messageLevel = cms.untracked.int32(0)
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('110X_mcRun4_realistic_v3'),
    pfnPrefix = cms.untracked.string('frontier://FrontierProd/'),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.pfNoPileUpJMETask = cms.Task(process.goodOfflinePrimaryVertices, process.pfNoPileUpJME, process.pfPileUpJME)


process.ak4caloHLTSequence = cms.Sequence((((((process.ak4caloHLTGenPtEta+process.ak4caloHLTPtEta)+process.ak4caloHLTPtEtaUncor)+process.ak4caloHLTJetToRef)+process.ak4caloHLTJetToUncorJet)+process.ak4caloHLT))


process.ak4pfHLTSequence = cms.Sequence((((((process.ak4pfHLTGenPtEta+process.ak4pfHLTPtEta)+process.ak4pfHLTPtEtaUncor)+process.ak4pfHLTJetToRef)+process.ak4pfHLTJetToUncorJet)+process.ak4pfHLT))


process.pfNoPileUpJMESequence = cms.Sequence(process.pfNoPileUpJMETask)


process.ak8caloHLTSequence = cms.Sequence((((((process.ak8caloHLTGenPtEta+process.ak8caloHLTPtEta)+process.ak8caloHLTPtEtaUncor)+process.ak8caloHLTJetToRef)+process.ak8caloHLTJetToUncorJet)+process.ak8caloHLT))


process.ak8pfHLTSequence = cms.Sequence((((((process.ak8pfHLTGenPtEta+process.ak8pfHLTPtEta)+process.ak8pfHLTPtEtaUncor)+process.ak8pfHLTJetToRef)+process.ak8pfHLTJetToUncorJet)+process.ak8pfHLT))


process.ak4pfHLTPath = cms.Path(process.ak4pfHLTSequence)


process.ak4caloHLTPath = cms.Path(process.ak4caloHLTSequence)


process.ak8pfHLTPath = cms.Path(process.ak8pfHLTSequence)


process.ak8caloHLTPath = cms.Path(process.ak8caloHLTSequence)


