from fastapi import APIRouter

from services.exchange import convert_currency

router = APIRouter(
    prefix="/convert",
    tags=["Convert"]
)

@router.get("")
def convert(from_currency: str, to_currency: str, amount: float):

    return convert_currency(from_currency, to_currency, amount)