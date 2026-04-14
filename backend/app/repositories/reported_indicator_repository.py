from sqlalchemy.orm import Session

from app.models.reported_indicator import ReportedIndicator
from app.repositories.base_repository import BaseRepository


class ReportedIndicatorRepository(BaseRepository[ReportedIndicator]):
    def __init__(self, db: Session):
        super().__init__(db, ReportedIndicator)

    def list_by_year(self, year: int):
        return self.db.query(ReportedIndicator).filter(ReportedIndicator.report_year == year).all()
