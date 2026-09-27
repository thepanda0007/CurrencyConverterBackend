from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import convert, trend, currencies

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

@app.get("/")
def home():
    return {"message": "Currency Converter API Running"}