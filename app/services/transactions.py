from fastapi import APIRouter
from app.schemas import TransactionList, TransactionParsedList, SalaryInput, ValidationResult
from app.utils.validators import validate_transactions
from app.utils.finance import parse_transactions

router = APIRouter()

@router.post("/parse", response_model=TransactionParsedList)
def parse_transactions_endpoint(data: TransactionList):
    parsed = parse_transactions(data.transactions)
    return {"transactions": parsed}

@router.post("/validator", response_model=ValidationResult)
def validator_endpoint(data: SalaryInput):
    return validate_transactions(data.transactions, data.salary)