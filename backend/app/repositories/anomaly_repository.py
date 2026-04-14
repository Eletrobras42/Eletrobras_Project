from sqlalchemy.orm import Session

from app.models.anomaly_record import AnomalyRecord
from app.repositories.base_repository import BaseRepository


class AnomalyRepository(BaseRepository[AnomalyRecord]):
    def __init__(self, db: Session):
        super().__init__(db, AnomalyRecord)

    def list_by_series_key(self, series_key: str):
        return self.db.query(AnomalyRecord).filter(AnomalyRecord.series_key == series_key).all()
