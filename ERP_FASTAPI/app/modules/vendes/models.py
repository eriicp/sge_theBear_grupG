from sqlalchemy import Column, Integer, String, Float
from database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    price_per_unit = Column(Float)
    total_price = Column(Float)