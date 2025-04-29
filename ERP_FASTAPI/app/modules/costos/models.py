from sqlalchemy import Column, Integer, String, Float
from database import Base

class Cost(Base):
    __tablename__ = "costos"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    amount = Column(Float, nullable=False)
    date = Column(String, index=True)  # Consider using a Date type for actual date values

    def __repr__(self):
        return f"<Cost(id={self.id}, description={self.description}, amount={self.amount}, date={self.date})>"