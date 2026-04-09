from datetime import datetime
from typing import List

from fastapi import APIRouter
from sqlalchemy import func
from app.database.connection import SessionLocal
from app.models.sensor_data import SensorData
from app.models.prediction_log import PredictionLog
from app.services.analytics_service import summarize_predictions, summarize_sensor_data, summarize_dashboard_overview

router = APIRouter(tags=["dashboard"])


@router.get("/overview")
def dashboard_overview():
    db = SessionLocal()
    try:
        sensor_rows = db.query(SensorData).all()
        prediction_rows = db.query(PredictionLog).all()

        sensor_summary = summarize_dashboard_overview(sensor_rows)
        prediction_summary = summarize_predictions(prediction_rows)

        return {
            "machine_count": sensor_summary["machine_count"],
            "record_count": sensor_summary["record_count"],
            "average_consumo_kwh": sensor_summary["average_consumo_kwh"],
            "average_temperature": sensor_summary["average_temperature"],
            "average_producao_hora": sensor_summary["average_producao_hora"],
            "production_efficiency": sensor_summary["production_efficiency"],
            "anomaly_rate": sensor_summary["anomaly_rate"],
            "prediction_count": prediction_summary["prediction_count"],
            "tolerance_rate": prediction_summary["tolerance_rate"],
            "total_predicted_consumo_kwh": round(sum(p.predicted_consumo_kwh for p in prediction_rows), 4),
            "total_anomaly_predictions": sum(1 for p in prediction_rows if p.anomalia),
            "last_prediction": prediction_summary["last_prediction"],
        }
    finally:
        db.close()


@router.get("/timeline")
def dashboard_timeline():
    db = SessionLocal()
    try:
        rows = (
            db.query(
                func.strftime("%Y-%m", SensorData.created_at).label("month"),
                func.count(SensorData.id).label("records"),
                func.avg(SensorData.consumo_kwh).label("avg_consumo"),
                func.avg(SensorData.producao_hora).label("avg_producao"),
            )
            .group_by("month")
            .order_by("month")
            .all()
        )

        return [
            {
                "month": row.month,
                "record_count": row.records,
                "average_consumo_kwh": round(row.avg_consumo, 4) if row.avg_consumo else None,
                "average_producao_hora": round(row.avg_producao, 4) if row.avg_producao else None,
            }
            for row in rows
        ]
    finally:
        db.close()
