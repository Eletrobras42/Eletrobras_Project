from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import PredictionService

router = APIRouter(tags=["predictions"])

@router.post("/predictions/interpolate", response_model=PredictionResponse)
def interpolate_prediction(request: PredictionRequest, db: Session = Depends(get_db)):
    result = PredictionService.interpolate_prediction(request, db)
    if result is None:
        raise HTTPException(status_code=404, detail="Dados insuficientes para interpolação")
    return result
