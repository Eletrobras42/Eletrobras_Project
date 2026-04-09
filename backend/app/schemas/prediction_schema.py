from typing import Optional

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    machine: str = Field(..., example="Linha 1")
    time: int = Field(..., example=75, description="Tempo em minutos")
    worker_activity_min: Optional[int] = Field(
        None,
        example=60,
        description="Tempo de atividade do colaborador em minutos",
    )


class PredictionResponse(BaseModel):
    machine: str
    time: int
    consumo_estimado: float
    erro_percentual: float
    fora_tolerancia: bool
    anomalia: bool
    history_count: int
    worker_activity_min: Optional[int] = None
    average_temperature: Optional[float] = None
    average_producao_hora: Optional[float] = None
