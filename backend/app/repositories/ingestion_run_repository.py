from sqlalchemy.orm import Session

from app.models.ingestion_run import IngestionRun
from app.repositories.base_repository import BaseRepository


class IngestionRunRepository(BaseRepository[IngestionRun]):
    def __init__(self, db: Session):
        super().__init__(db, IngestionRun)

    def list_recent(self, limit: int = 10):
        return self.db.query(IngestionRun).order_by(IngestionRun.started_at.desc()).limit(limit).all()
