from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.ingestion_run import IngestionRunRequest, IngestionRunResponse
from app.services.ingestion_service import IngestionService

router = APIRouter(tags=["ingestion"])

@router.post("/ingestion/run", response_model=IngestionRunResponse)
def run_ingestion(request: IngestionRunRequest, db: Session = Depends(get_db)):
    result = IngestionService.run_ingestion(db, request.source_document_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Documento de origem não encontrado")
    return result
