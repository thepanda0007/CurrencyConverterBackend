from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Conversion(Base):
    __tablename__ = "conversions"

    id = Column(Integer, primary_key=True, index=True)
    from_currency = Column(String)
    to_currency = Column(String)
    amount = Column(Float)
    rate = Column(Float)
    converted_amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    from_currency = Column(String, nullable=False)
    to_currency = Column(String, nullable=False)