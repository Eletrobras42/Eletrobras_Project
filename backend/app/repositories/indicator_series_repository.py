from sqlalchemy.orm import Session

from app.models.indicator_series import IndicatorSeries
from app.repositories.base_repository import BaseRepository


class IndicatorSeriesRepository(BaseRepository[IndicatorSeries]):
    def __init__(self, db: Session):
        super().__init__(db, IndicatorSeries)

    def list_by_series_key(self, series_key: str):
        return self.db.query(IndicatorSeries).filter(IndicatorSeries.series_key == series_key).order_by(IndicatorSeries.observation_year).all()

    def list_all_series(self):
        return self.db.query(IndicatorSeries).order_by(IndicatorSeries.series_key, IndicatorSeries.observation_year).all()
