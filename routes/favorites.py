from fastapi import APIRouter
from services.exchange import (
    get_favorites,
    add_favorite,
    delete_favorite
)

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)


@router.get("")
def favorites():
    return get_favorites()


@router.post("")
def save_favorite(from_currency: str, to_currency: str):
    return add_favorite(from_currency, to_currency)


@router.delete("/{favorite_id}")
def remove_favorite(favorite_id: int):
    return delete_favorite(favorite_id)