from typing import List, Optional

from fastapi import APIRouter, HTTPException
from sqlalchemy import func
from app.database.connection import SessionLocal
from app.models.prediction_log import PredictionLog
from app.models.sensor_data import SensorData
from app.schemas.analytics_schema import (
    AnalyticsResponse,
    MachineSummaryResponse,
    PredictionLogItem,
)
from app.services.analytics_service import summarize_predictions, summarize_sensor_data

router = APIRouter(tags=["analytics"])


@router.get("/machines", response_model=List[MachineSummaryResponse])
def list_machines():
    db = SessionLocal()
    try:
        rows = (
            db.query(SensorData.machine_name, func.count(SensorData.id).label("record_count"))
            .group_by(SensorData.machine_name)
            .order_by(SensorData.machine_name)
            .all()
        )

        return [
            MachineSummaryResponse(
                machine_name=row[0],
                record_count=row[1],
                average_consumo_kwh=0.0,
                average_temperature=None,
                average_producao_hora=None,
            )
            for row in rows
        ]
    finally:
        db.close()


@router.get("/analytics", response_model=AnalyticsResponse)
def machine_analytics(machine: str):
    db = SessionLocal()
    try:
        sensor_rows = (
            db.query(SensorData)
            .filter(SensorData.machine_name == machine)
            .order_by(SensorData.timestamp_min)
            .all()
        )

        if not sensor_rows:
            raise HTTPException(status_code=404, detail="Máquina não encontrada")

        predictions = (
            db.query(PredictionLog)
            .filter(PredictionLog.machine_name == machine)
            .order_by(PredictionLog.created_at)
            .all()
        )

        sensor_summary = summarize_sensor_data(sensor_rows)
        prediction_summary = summarize_predictions(predictions)

        return AnalyticsResponse(
            machine_name=machine,
            record_count=sensor_summary["record_count"],
            average_consumo_kwh=sensor_summary["average_consumo_kwh"],
            min_consumo_kwh=sensor_summary["min_consumo_kwh"],
            max_consumo_kwh=sensor_summary["max_consumo_kwh"],
            average_temperature=sensor_summary["average_temperature"],
            average_producao_hora=sensor_summary["average_producao_hora"],
            anomaly_rate=round(
                sensor_summary["anomaly_count"] / sensor_summary["record_count"] * 100
                if sensor_summary["record_count"] > 0
                else 0.0,
                2,
            ),
            prediction_count=prediction_summary["prediction_count"],
            tolerance_rate=prediction_summary["tolerance_rate"],
            last_prediction=prediction_summary["last_prediction"],
        )
    finally:
        db.close()


@router.get("/predictions", response_model=List[PredictionLogItem])
def prediction_history(machine: Optional[str] = None):
    db = SessionLocal()
    try:
        query = db.query(PredictionLog)
        if machine:
            query = query.filter(PredictionLog.machine_name == machine)
        rows = query.order_by(PredictionLog.created_at.desc()).all()

        return [
            PredictionLogItem(
                machine_name=row.machine_name,
                timestamp_min=row.timestamp_min,
                predicted_consumo_kwh=row.predicted_consumo_kwh,
                erro_percentual=row.erro_percentual,
                fora_tolerancia=row.fora_tolerancia,
                anomalia=row.anomalia,
                created_at=row.created_at,
            )
            for row in rows
        ]
    finally:
        db.close()
