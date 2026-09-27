from fastapi import APIRouter
from services.exchange import get_travel_budget

router = APIRouter(
    prefix="/travel-budget",
    tags=["Travel Budget"]
)

@router.get("")
def travel_budget(base_currency: str, amount: float):
    return get_travel_budget(base_currency, amount)