from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Transaction(BaseModel):
    datetime: datetime
    amount: float

class TransactionParsed(Transaction):
    ceiling: float
    remanent: float

class TransactionList(BaseModel):
    transactions: List[Transaction]

class TransactionParsedList(BaseModel):
    transactions: List[TransactionParsed]

class SalaryInput(BaseModel):
    transactions: List[TransactionParsed]
    salary: float

class ValidationResult(BaseModel):
    valid: List[TransactionParsed]
    invalid: List[str]

class DateRange(BaseModel):
    start: datetime
    end: datetime

class FilterInput(BaseModel):
    transactions: List[TransactionParsed]
    q: List[DateRange]
    p: List[DateRange]
    k: List[DateRange]

class FilterResult(BaseModel):
    valid: List[TransactionParsed]
    invalid: List[TransactionParsed]

class ReturnsInput(BaseModel):
    age: int
    salary: float
    inflation: float = 0.0483
    transactions: List[TransactionParsed]
    q: List[DateRange]
    p: List[DateRange]
    k: List[DateRange]

class ReturnsOutput(BaseModel):
    total_ppr: float
    total_ishares: float
    total_savings: float
    adjusted_for_inflation: float

class PerformanceMetrics(BaseModel):
    memory_usage_mb: float
    execution_time_ms: float
    threads: int
