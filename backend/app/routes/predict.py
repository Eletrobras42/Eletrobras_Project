from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.prediction_schema import PredictionRequest, PredictionResponse
from app.services.prediction_service import build_prediction
from app.database.connection import SessionLocal
from app.models.sensor_data import SensorData
from app.models.prediction_log import PredictionLog

router = APIRouter(tags=["prediction"])


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    db = SessionLocal()
    try:
        sensor_rows = (
            db.query(SensorData)
            .filter(SensorData.machine_name == request.machine)
            .order_by(SensorData.timestamp_min)
            .all()
        )

        if len(sensor_rows) < 2:
            raise HTTPException(
                status_code=404,
                detail="Dados históricos insuficientes para a máquina informada",
            )

        timestamps = [row.timestamp_min for row in sensor_rows]
        consumos = [row.consumo_kwh for row in sensor_rows]
        temperature_values = [row.temperatura for row in sensor_rows if row.temperatura is not None]
        production_values = [row.producao_hora for row in sensor_rows if row.producao_hora is not None]

        prediction = build_prediction(request.time, timestamps, consumos)
        average_temperature = (
            round(sum(temperature_values) / len(temperature_values), 2)
            if temperature_values
            else None
        )
        average_producao_hora = (
            round(sum(production_values) / len(production_values), 2)
            if production_values
            else None
        )

        log = PredictionLog(
            machine_name=request.machine,
            timestamp_min=request.time,
            predicted_consumo_kwh=prediction["predicted_consumo_kwh"],
            erro_percentual=prediction["erro_percentual"],
            fora_tolerancia=prediction["fora_tolerancia"],
            anomalia=prediction["anomalia"],
            created_at=datetime.utcnow(),
        )

        db.add(log)
        db.commit()
        db.refresh(log)

        return PredictionResponse(
            machine=request.machine,
            time=request.time,
            consumo_estimado=prediction["predicted_consumo_kwh"],
            erro_percentual=prediction["erro_percentual"],
            fora_tolerancia=prediction["fora_tolerancia"],
            anomalia=prediction["anomalia"],
            history_count=len(sensor_rows),
            worker_activity_min=request.worker_activity_min,
            average_temperature=average_temperature,
            average_producao_hora=average_producao_hora,
        )
    finally:
        db.close()


@router.get("/history")
def history(machine: str):
    db = SessionLocal()
    try:
        sensor_rows = (
            db.query(SensorData)
            .filter(SensorData.machine_name == machine)
            .order_by(SensorData.timestamp_min)
            .all()
        )
        return [
            {
                "machine_name": row.machine_name,
                "timestamp_min": row.timestamp_min,
                "consumo_kwh": row.consumo_kwh,
                "temperatura": row.temperatura,
                "producao_hora": row.producao_hora,
                "worker_activity_min": row.worker_activity_min,
                "status": row.status,
            }
            for row in sensor_rows
        ]
    finally:
        db.close()
