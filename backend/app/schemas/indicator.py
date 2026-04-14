from pydantic import BaseModel, ConfigDict


class IndicatorResponse(BaseModel):
    id: int
    report_year: int
    indicator_code: str | None = None
    indicator_name: str
    indicator_category: str | None = None
    metric_unit: str | None = None
    numeric_value: float | None = None
    model_config = ConfigDict(from_attributes=True)


class IndicatorSeriesResponse(BaseModel):
    id: int
    series_key: str
    indicator_name: str
    observation_year: int
    numeric_value: float | None = None
    is_interpolated: bool
    model_config = ConfigDict(from_attributes=True)


class TrendResponse(BaseModel):
    series_key: str
    indicator_name: str
    observation_year: int
    numeric_value: float | None = None
    is_interpolated: bool

    @classmethod
    def from_series(cls, series_key: str, trends: list[IndicatorSeriesResponse]):
        if not trends:
            raise ValueError("Trends must contain at least one entry")
        return cls(
            series_key=series_key,
            indicator_name=trends[0].indicator_name,
            observation_year=trends[-1].observation_year,
            numeric_value=trends[-1].numeric_value,
            is_interpolated=trends[-1].is_interpolated,
        )
