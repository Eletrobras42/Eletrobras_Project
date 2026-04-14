from typing import List, Dict, Any
from sqlalchemy.orm import Session

from app.repositories.sensor_data_repository import SensorDataRepository
from app.repositories.prediction_log_repository import PredictionLogRepository


class AnalyticsRepository:
    """Repository for analytics operations."""
    
    def __init__(self, db: Session):
        self.sensor_repo = SensorDataRepository(db)
        self.prediction_repo = PredictionLogRepository(db)
    
    def get_sensor_data_by_machine(self, machine_name: str) -> List[Any]:
        """Get all sensor data for a machine."""
        return self.sensor_repo.get_by_machine(machine_name)
    
    def get_predictions_by_machine(self, machine_name: str) -> List[Any]:
        """Get all predictions for a machine."""
        return self.prediction_repo.get_by_machine(machine_name)
    
    def get_all_machines_summary(self) -> List[Dict[str, Any]]:
        """Get summary of all machines."""
        return self.sensor_repo.get_machines_summary()
    
    def get_all_sensor_data(self) -> List[Any]:
        """Get all sensor data."""
        return self.sensor_repo.get_all()
    
    def get_all_predictions(self) -> List[Any]:
        """Get all predictions."""
        return self.prediction_repo.get_all()
    
    def get_timeline_data(self) -> List[Dict[str, Any]]:
        """Get timeline data grouped by month."""
        return self.sensor_repo.get_timeline_data()
    
    def get_anomalies(self, machine_name: str = None) -> List[Any]:
        """Get anomalies, optionally filtered by machine."""
        return self.prediction_repo.get_anomalies(machine_name)
    
    def get_out_of_tolerance(self, machine_name: str = None) -> List[Any]:
        """Get predictions out of tolerance, optionally filtered by machine."""
        return self.prediction_repo.get_out_of_tolerance(machine_name)
