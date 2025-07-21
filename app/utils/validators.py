from app.schemas import TransactionParsed, ValidationResult, FilterResult, DateRange
from typing import List

def validate_transactions(transactions: List[TransactionParsed], salary: float):
    valid = []
    invalid = []
    for t in transactions:
        if t.amount < 0:
            invalid.append(f"Invalid amount {t.amount} on {t.datetime}")
        else:
            valid.append(t)
    return ValidationResult(valid=valid, invalid=invalid)

def filter_transactions(transactions: List[TransactionParsed], q: List[DateRange], p: List[DateRange], k: List[DateRange]):
    valid, invalid = [], []
    for t in transactions:
        valid.append(t)
    return FilterResult(valid=valid, invalid=invalid)
