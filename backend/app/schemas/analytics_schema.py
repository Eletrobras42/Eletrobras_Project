from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MachineSummaryResponse(BaseModel):
    machine_name: str
    record_count: int
    average_consumo_kwh: float
    average_temperature: Optional[float]
    average_producao_hora: Optional[float]


class PredictionLogItem(BaseModel):
    machine_name: str
    timestamp_min: int
    predicted_consumo_kwh: float
    erro_percentual: float
    fora_tolerancia: bool
    anomalia: bool
    created_at: datetime


class LastPredictionSummary(BaseModel):
    timestamp_min: int
    predicted_consumo_kwh: float
    erro_percentual: float
    fora_tolerancia: bool
    anomalia: bool
    created_at: datetime


class AnalyticsResponse(BaseModel):
    machine_name: str
    record_count: int
    average_consumo_kwh: float
    min_consumo_kwh: float
    max_consumo_kwh: float
    average_temperature: Optional[float]
    average_producao_hora: Optional[float]
    anomaly_rate: float
    prediction_count: int
    tolerance_rate: float
    last_prediction: Optional[LastPredictionSummary]
