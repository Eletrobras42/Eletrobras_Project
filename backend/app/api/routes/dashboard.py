from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.dashboard import KpiResponse, TrendResponse
from app.services.kpi_service import KpiService
from app.services.indicator_service import IndicatorService

router = APIRouter(tags=["dashboard"])

@router.get("/dashboard/kpis", response_model=KpiResponse)
def get_dashboard_kpis(db: Session = Depends(get_db)):
    return KpiService.get_kpis(db)

@router.get("/dashboard/trends", response_model=List[TrendResponse])
def get_dashboard_trends(db: Session = Depends(get_db)):
    return IndicatorService.get_series_trends(db)
