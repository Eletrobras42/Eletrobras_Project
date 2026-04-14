from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session

T = TypeVar('T')


class BaseRepository(Generic[T]):
    """Base repository class for database operations."""
    
    def __init__(self, db: Session, model: type[T]):
        self.db = db
        self.model = model
    
    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self) -> List[T]:
        return self.db.query(self.model).all()
    
    def create(self, obj: T) -> T:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj: T) -> T:
        self.db.merge(obj)
        self.db.commit()
        return obj
    
    def delete(self, id: int) -> bool:
        obj = self.get_by_id(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()
            return True
        return False
    
    def close(self):
        self.db.close()
