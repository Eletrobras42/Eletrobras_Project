from pydantic import BaseModel


class KpiResponse(BaseModel):
    documents_cataloged: int
    indicators_extracted: int
    series_consolidated: int
    anomalies_detected: int
    ingestion_runs: int


class TrendResponse(BaseModel):
    series_key: str
    indicator_name: str
    observation_year: int
    numeric_value: float | None = None
    is_interpolated: bool
