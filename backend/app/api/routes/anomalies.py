from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.anomaly import AnomalyResponse
from app.services.anomaly_service import AnomalyService

router = APIRouter(tags=["anomalies"])

@router.get("/dashboard/anomalies", response_model=list[AnomalyResponse])
def list_anomalies(db: Session = Depends(get_db)):
    return AnomalyService.list_anomalies(db)
