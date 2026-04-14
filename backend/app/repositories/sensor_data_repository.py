from typing import List, Optional, Dict, Any
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.sensor_data import SensorData
from app.repositories.base_repository import BaseRepository


class SensorDataRepository(BaseRepository[SensorData]):
    """Repository for SensorData model."""
    
    def __init__(self, db: Session):
        super().__init__(db, SensorData)
    
    def get_by_machine(self, machine_name: str, limit: Optional[int] = None) -> List[SensorData]:
        """Get all sensor data for a machine."""
        query = self.db.query(SensorData).filter(
            SensorData.machine_name == machine_name
        ).order_by(SensorData.timestamp_min)
        
        if limit:
            query = query.limit(limit)
        
        return query.all()
    
    def get_machines_summary(self) -> List[Dict[str, Any]]:
        """Get summary of all machines with record counts."""
        rows = (
            self.db.query(
                SensorData.machine_name, 
                func.count(SensorData.id).label("record_count")
            )
            .group_by(SensorData.machine_name)
            .order_by(SensorData.machine_name)
            .all()
        )
        
        return [
            {
                "machine_name": row[0],
                "record_count": row[1],
            }
            for row in rows
        ]
    
    def get_timeline_data(self) -> List[Dict[str, Any]]:
        """Get timeline data grouped by month."""
        rows = (
            self.db.query(
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
