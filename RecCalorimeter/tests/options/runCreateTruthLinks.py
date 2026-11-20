from Configurables import CreateTruthLinks, EventDataSvc
from k4FWCore import ApplicationMgr, IOSvc

io_svc = IOSvc("IOSvc")
io_svc.Input = "truth_link_events.edm4hep.root"
io_svc.Output = "truth_links.edm4hep.root"

create_truth_links = CreateTruthLinks(
    "CreateTruthLinks",
    cell_hit_links=["ECalLinks", "HCalLinks"],
    clusters=["Clusters"],
    mcparticles="MCParticles",
    cell_mcparticle_links="CaloHitMCParticleLinks",
    cluster_mcparticle_links="ClusterMCParticleLinks",
)

ApplicationMgr(
    TopAlg=[create_truth_links],
    EvtSel="NONE",
    EvtMax=-1,
    ExtSvc=[EventDataSvc("EventDataSvc")],
)
