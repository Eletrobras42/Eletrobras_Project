from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.indicator import IndicatorResponse, IndicatorSeriesResponse
from app.services.indicator_service import IndicatorService

router = APIRouter(tags=["indicators"])

@router.get("/indicators", response_model=List[IndicatorResponse])
def list_indicators(db: Session = Depends(get_db)):
    return IndicatorService.list_indicators(db)

@router.get("/indicators/series", response_model=List[IndicatorSeriesResponse])
def list_indicator_series(db: Session = Depends(get_db)):
    return IndicatorService.list_indicator_series(db)
