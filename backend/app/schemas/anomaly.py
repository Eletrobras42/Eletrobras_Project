from pydantic import BaseModel, ConfigDict


class AnomalyResponse(BaseModel):
    series_key: str
    anomaly_date: str | None = None
    anomaly_year: int | None = None
    observed_value: float | None = None
    expected_value: float | None = None
    anomaly_score: float | None = None
    anomaly_type: str
    severity: str | None = None
    model_name: str | None = None
    explanation: str | None = None
    model_config = ConfigDict(from_attributes=True)
