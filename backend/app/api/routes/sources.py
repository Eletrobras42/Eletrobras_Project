from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.source_document import SourceDocumentResponse
from app.services.catalog_service import CatalogService

router = APIRouter(tags=["sources"])

@router.get("/sources", response_model=list[SourceDocumentResponse])
def get_sources(db: Session = Depends(get_db)):
    return CatalogService.list_sources(db)

@router.post("/sources/seed", response_model=list[SourceDocumentResponse])
def seed_sources(db: Session = Depends(get_db)):
    return CatalogService.seed_default_sources(db)
