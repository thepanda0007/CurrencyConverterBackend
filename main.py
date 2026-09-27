from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import convert, trend, currencies, travel_budget, favorites

from database import engine
from models import Base
from database import SessionLocal
from models import Conversion


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Currency Converter API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(convert.router)
app.include_router(trend.router)
app.include_router(currencies.router)
app.include_router(travel_budget.router)
app.include_router(favorites.router)

@app.get("/")
def home():
    return {"message": "Currency Converter API Running"}

@app.get("/history")
def history():
    db = SessionLocal()

    data = db.query(Conversion)\
             .order_by(Conversion.created_at.desc())\
             .all()

    db.close()
    return data