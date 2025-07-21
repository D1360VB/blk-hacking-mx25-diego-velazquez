from fastapi import APIRouter
from app.schemas import FilterInput, FilterResult
from app.utils.validators import filter_transactions

router = APIRouter()

@router.post("/filter", response_model=FilterResult)
def filter_endpoint(data: FilterInput):
    return filter_transactions(data.transactions, data.q, data.p, data.k)