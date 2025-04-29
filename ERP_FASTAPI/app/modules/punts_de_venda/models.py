from sqlalchemy import Column, Integer, String
from database import Base

class PointOfSale(Base):
    __tablename__ = "points_of_sale"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    contact_number = Column(String)