from fastapi import APIRouter, Depends
from app.db.session import get_db
from app.services.analytics.funnel_engine import FunnelEngine
from app.services.analytics.retention_engine import RetentionEngine
from app.services.analytics.live_dashboard import LiveDashboard

router = APIRouter()


@router.get("/funnel")
def funnel(db=Depends(get_db), tenant_id: str = None):

    engine = FunnelEngine()
    return engine.get_funnel(db, tenant_id)


@router.get("/retention")
def retention(db=Depends(get_db), tenant_id: str = None):

    engine = RetentionEngine()
    return engine.get_retention(db, tenant_id)


@router.get("/live")
def live(db=Depends(get_db), tenant_id: str = None):

    engine = LiveDashboard()
    return engine.get_live_stats(db, tenant_id)