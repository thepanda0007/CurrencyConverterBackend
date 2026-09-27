from fastapi import APIRouter

from services.exchange import get_trend

router = APIRouter(
    prefix="/trend",
    tags=["Trend"]
)

@router.get("")
def trend(from_currency: str, to_currency: str, days: int = 7):

    return get_trend(from_currency, to_currency, days)