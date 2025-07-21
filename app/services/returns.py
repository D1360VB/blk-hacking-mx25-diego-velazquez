from fastapi import APIRouter
from app.schemas import ReturnsInput, ReturnsOutput
from app.utils.finance import calculate_returns

router = APIRouter()

@router.post("/returns:ppr", response_model=ReturnsOutput)
def ppr_returns_endpoint(data: ReturnsInput):
    return calculate_returns(data, investment_type="ppr")

@router.post("/returns:ishares", response_model=ReturnsOutput)
def ishares_returns_endpoint(data: ReturnsInput):
    return calculate_returns(data, investment_type="ishares")