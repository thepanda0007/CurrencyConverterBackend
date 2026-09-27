import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
from database import SessionLocal
from models import Favorite

API_KEY = os.getenv("EXCHANGERATEAPI")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

def get_supported_currencies():

    url = f"{BASE_URL}/codes"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()


def convert_currency(from_currency, to_currency, amount):

    url = f"{BASE_URL}/pair/{from_currency}/{to_currency}/{amount}"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()


import requests
from datetime import datetime, timedelta
import os

API_KEY = os.getenv("EXCHANGERATEAPI")
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

def get_trend(from_currency, to_currency, days=30):
    end_date = datetime.now().date()
    results = []

    for i in range(days):
        date = end_date - timedelta(days=days - 1 - i)

        url = (
            f"{BASE_URL}/history/"
            f"{from_currency}/"
            f"{date.year}/{date.month}/{date.day}"
        )

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        results.append({
            "date": str(date),
            "rate": data["conversion_rates"][to_currency]
        })

    return results

def get_travel_budget(base_currency, amount):
    url = f"{BASE_URL}/latest/{base_currency}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    major_currencies = ["USD", "EUR", "GBP", "JPY", "AUD"]

    results = []

    for currency in major_currencies:
        if currency in data["conversion_rates"]:
            results.append({
                "currency": currency,
                "value": round(data["conversion_rates"][currency] * amount, 2)
            })

    return {
        "base": base_currency,
        "amount": amount,
        "results": results
    }


def get_favorites():
    db = SessionLocal()

    favorites = db.query(Favorite).all()

    db.close()

    return favorites


def add_favorite(from_currency, to_currency):
    db = SessionLocal()

    # Prevent duplicates
    existing = (
        db.query(Favorite)
        .filter(
            Favorite.from_currency == from_currency,
            Favorite.to_currency == to_currency
        )
        .first()
    )

    if existing:
        db.close()
        return existing

    favorite = Favorite(
        from_currency=from_currency,
        to_currency=to_currency
    )

    db.add(favorite)
    db.commit()
    db.refresh(favorite)

    db.close()

    return favorite


def delete_favorite(favorite_id):
    db = SessionLocal()

    favorite = db.query(Favorite).filter(Favorite.id == favorite_id).first()

    if favorite:
        db.delete(favorite)
        db.commit()

    db.close()

    return {"message": "Favorite deleted"}