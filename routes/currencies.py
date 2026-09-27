from fastapi import APIRouter

from services.exchange import get_supported_currencies

router = APIRouter(
    prefix="/currencies",
    tags=["Currencies"]
)

@router.get("")
def currencies():
    return get_supported_currencies()