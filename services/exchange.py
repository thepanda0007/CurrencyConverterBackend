import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

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


def get_trend(from_currency, to_currency, days):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=days-1)

    url = (
        f"https://api.frankfurter.app/"
        f"{start_date}..{end_date}"
        f"?from={from_currency}&to={to_currency}"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    results = []

    for date in sorted(data["rates"].keys()):
        results.append({
            "date": date,
            "rate": data["rates"][date][to_currency]
        })

    return results