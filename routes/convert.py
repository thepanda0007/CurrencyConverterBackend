from fastapi import APIRouter
from services.exchange import convert_currency
from database import SessionLocal
from models import Conversion

router = APIRouter(
    prefix="/convert",
    tags=["Convert"]
)

@router.get("")
def convert(from_currency: str, to_currency: str, amount: float):

    result = convert_currency(from_currency, to_currency, amount)

    db = SessionLocal()

    db.add(
        Conversion(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            rate=result["conversion_rate"],
            converted_amount=result["conversion_result"]
        )
    )

    db.commit()

    latest_ids = [
        row.id for row in db.query(Conversion.id)
        .order_by(Conversion.created_at.desc())
        .limit(10)
        .all()
    ]

    db.query(Conversion).filter(
        ~Conversion.id.in_(latest_ids)
    ).delete(synchronize_session=False)

    db.commit()
    db.close()

    return result