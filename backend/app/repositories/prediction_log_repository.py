from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session

from app.models.prediction_log import PredictionLog
from app.repositories.base_repository import BaseRepository


class PredictionLogRepository(BaseRepository[PredictionLog]):
    """Repository for PredictionLog model."""
    
    def __init__(self, db: Session):
        super().__init__(db, PredictionLog)
    
    def get_by_machine(self, machine_name: str, limit: Optional[int] = None) -> List[PredictionLog]:
        """Get all predictions for a machine."""
        query = self.db.query(PredictionLog).filter(
            PredictionLog.machine_name == machine_name
        ).order_by(PredictionLog.created_at)
        
        if limit:
            query = query.limit(limit)
        
        return query.all()
    
    def get_latest_by_machine(self, machine_name: str) -> Optional[PredictionLog]:
        """Get the latest prediction for a machine."""
        return (
            self.db.query(PredictionLog)
            .filter(PredictionLog.machine_name == machine_name)
            .order_by(PredictionLog.created_at.desc())
            .first()
        )
    
    def get_anomalies(self, machine_name: Optional[str] = None) -> List[PredictionLog]:
        """Get all anomalies, optionally filtered by machine."""
        query = self.db.query(PredictionLog).filter(PredictionLog.anomalia == True)
        
        if machine_name:
            query = query.filter(PredictionLog.machine_name == machine_name)
        
        return query.order_by(PredictionLog.created_at.desc()).all()
    
    def get_out_of_tolerance(self, machine_name: Optional[str] = None) -> List[PredictionLog]:
        """Get all predictions out of tolerance, optionally filtered by machine."""
        query = self.db.query(PredictionLog).filter(PredictionLog.fora_tolerancia == True)
        
        if machine_name:
            query = query.filter(PredictionLog.machine_name == machine_name)
        
        return query.order_by(PredictionLog.created_at.desc()).all()
