from app.schemas import Transaction, TransactionParsed
from typing import List
from math import ceil

def parse_transactions(transactions: List[Transaction]) -> List[TransactionParsed]:
    parsed = []
    for t in transactions:
        ceiling_amount = ceil(t.amount / 100) * 100
        remanent = ceiling_amount - t.amount
        parsed.append(TransactionParsed(
            date=t.datetime,
            amount=t.amount,
            ceiling=ceiling_amount,
            remanent=remanent
        ))
    return parsed

def calculate_returns(data, investment_type: str):
    age = data.age
    salary = data.salary
    inflation = data.inflation
    transactions = data.transactions

    total_remanent = sum(t.remanent for t in transactions)
    years = max(65 - age, 0)

    ppr_limit = salary * 0.10
    ppr = min(total_remanent, ppr_limit)
    ishares = max(total_remanent - ppr, 0)

    r = 0.05
    if investment_type == "ppr":
        future_value = ppr * ((1 + r) ** years)
    else:
        future_value = ishares * ((1 + r) ** years)

    future_value_adjusted = future_value / ((1 + inflation) ** years)

    return {
        "total_ppr": ppr,
        "total_ishares": ishares,
        "total_savings": total_remanent,
        "adjusted_for_inflation": future_value_adjusted
    }
