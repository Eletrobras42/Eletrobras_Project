from typing import List

from sqlalchemy.orm import Session

from app.repositories.indicator_series_repository import IndicatorSeriesRepository
from app.repositories.reported_indicator_repository import ReportedIndicatorRepository
from app.schemas.indicator import IndicatorResponse, IndicatorSeriesResponse, TrendResponse


class IndicatorService:
    @staticmethod
    def list_indicators(db: Session) -> List[IndicatorResponse]:
        repository = ReportedIndicatorRepository(db)
        rows = repository.get_all()
        return [
            IndicatorResponse(
                id=row.id,
                report_year=row.report_year,
                indicator_code=row.indicator_code,
                indicator_name=row.indicator_name,
                indicator_category=row.indicator_category,
                metric_unit=row.metric_unit,
                numeric_value=row.numeric_value,
            )
            for row in rows
        ]

    @staticmethod
    def list_indicator_series(db: Session) -> List[IndicatorSeriesResponse]:
        repository = IndicatorSeriesRepository(db)
        rows = repository.get_all()
        return [
            IndicatorSeriesResponse(
                id=row.id,
                series_key=row.series_key,
                indicator_name=row.indicator_name,
                observation_year=row.observation_year,
                numeric_value=row.numeric_value,
                is_interpolated=row.is_interpolated == 1,
            )
            for row in rows
        ]

    @staticmethod
    def get_series_trends(db: Session) -> List[TrendResponse]:
        repository = IndicatorSeriesRepository(db)
        rows = repository.list_all_series()
        trends: dict[str, list[IndicatorSeriesResponse]] = {}

        for row in rows:
            trend = TrendResponse(
                series_key=row.series_key,
                indicator_name=row.indicator_name,
                observation_year=row.observation_year,
                numeric_value=row.numeric_value,
                is_interpolated=row.is_interpolated == 1,
            )
            trends.setdefault(row.series_key, []).append(trend)

        return [TrendResponse.from_series(key, items) for key, items in trends.items()]
