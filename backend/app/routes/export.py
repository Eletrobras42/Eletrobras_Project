import csv
import io

from fastapi import APIRouter, Response
from app.database.connection import SessionLocal
from app.models.sensor_data import SensorData
from app.models.prediction_log import PredictionLog

router = APIRouter(tags=["export"])


@router.get("/sensor-data", response_class=Response)
def export_sensor_data_csv():
    db = SessionLocal()
    try:
        rows = db.query(SensorData).order_by(SensorData.machine_name, SensorData.timestamp_min).all()
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow([
            "machine_name",
            "timestamp_min",
            "consumo_kwh",
            "temperatura",
            "producao_hora",
            "worker_activity_min",
            "status",
            "created_at",
            "extra_data",
        ])

        for row in rows:
            writer.writerow([
                row.machine_name,
                row.timestamp_min,
                row.consumo_kwh,
                row.temperatura,
                row.producao_hora,
                row.worker_activity_min,
                row.status,
                row.created_at,
                row.extra_data,
            ])

        return Response(content=buffer.getvalue(), media_type="text/csv")
    finally:
        db.close()


@router.get("/predictions", response_class=Response)
def export_predictions_csv():
    db = SessionLocal()
    try:
        rows = db.query(PredictionLog).order_by(PredictionLog.machine_name, PredictionLog.created_at).all()
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow([
            "machine_name",
            "timestamp_min",
            "predicted_consumo_kwh",
            "erro_percentual",
            "fora_tolerancia",
            "anomalia",
            "created_at",
        ])

        for row in rows:
            writer.writerow([
                row.machine_name,
                row.timestamp_min,
                row.predicted_consumo_kwh,
                row.erro_percentual,
                row.fora_tolerancia,
                row.anomalia,
                row.created_at,
            ])

        return Response(content=buffer.getvalue(), media_type="text/csv")
    finally:
        db.close()
