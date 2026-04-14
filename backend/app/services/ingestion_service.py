from datetime import datetime
from sqlalchemy.orm import Session

from app.models.ingestion_run import IngestionRun
from app.models.source_document import SourceDocument
from app.repositories.ingestion_run_repository import IngestionRunRepository
from app.repositories.source_repository import SourceDocumentRepository


class IngestionService:
    @staticmethod
    def run_ingestion(db: Session, source_document_id: int):
        source_repo = SourceDocumentRepository(db)
        ingestion_repo = IngestionRunRepository(db)

        source = source_repo.get_by_id(source_document_id)
        if source is None:
            return None

        run = IngestionRun(
            status="running",
            source_document_id=source_document_id,
            started_at=datetime.utcnow(),
            pipeline_version="1.0",
        )
        db.add(run)
        db.commit()
        db.refresh(run)

        try:
            run.rows_extracted = 0
            run.rows_loaded = 0
            run.status = "completed"
            run.finished_at = datetime.utcnow()
            ingestion_repo.update(run)
        except Exception as exc:
            run.status = "failed"
            run.execution_log = str(exc)
            run.finished_at = datetime.utcnow()
            ingestion_repo.update(run)

        return run
