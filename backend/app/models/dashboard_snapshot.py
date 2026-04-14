import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base


class DashboardSnapshot(Base):
    __tablename__ = "dashboard_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    snapshot_name = Column(String, nullable=False)
    snapshot_scope = Column(String, nullable=True)
    payload_json = Column(Text, nullable=False)
    generated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
