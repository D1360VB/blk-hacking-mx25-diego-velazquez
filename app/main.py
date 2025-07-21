from fastapi import FastAPI
from app.services import transactions, filters, returns, performance

app = FastAPI(title="BlackRock Challenge API")

app.include_router(transactions.router, prefix="/blackrock/challenge/v1/transactions")
app.include_router(filters.router, prefix="/blackrock/challenge/v1/transactions")
app.include_router(returns.router, prefix="/blackrock/challenge/v1")
app.include_router(performance.router, prefix="/blackrock/challenge/v1")