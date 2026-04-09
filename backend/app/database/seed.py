import csv
import json
import os
from app.database.connection import SessionLocal
from app.models.sensor_data import SensorData


def seed_initial_data() -> None:
    db = SessionLocal()
    try:
        existing_count = db.query(SensorData).count()
        if existing_count > 0:
            return

        root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        csv_path = os.path.join(root, "data", "eletrobras_consumo_historico.csv")

        if not os.path.exists(csv_path):
            return

        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                known_fields = {"machine_name", "timestamp_min", "consumo_kwh", "temperatura", "producao_hora", "worker_activity_min", "status"}
                extra = {
                    key: value
                    for key, value in row.items()
                    if key not in known_fields and value is not None and value != ""
                }

                db.add(
                    SensorData(
                        machine_name=row["machine_name"],
                        timestamp_min=int(row["timestamp_min"]),
                        consumo_kwh=float(row["consumo_kwh"]),
                        temperatura=float(row["temperatura"]) if row.get("temperatura") else None,
                        producao_hora=float(row["producao_hora"]) if row.get("producao_hora") else None,
                        worker_activity_min=int(row["worker_activity_min"])
                        if row.get("worker_activity_min")
                        else None,
                        status=row.get("status"),
                        extra_data=json.dumps(extra) if extra else None,
                    )
                )
            db.commit()
    finally:
        db.close()
