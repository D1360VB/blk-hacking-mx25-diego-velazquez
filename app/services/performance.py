from fastapi import APIRouter
from app.schemas import PerformanceMetrics
import psutil
import threading
import time

router = APIRouter()

@router.get("/performance", response_model=PerformanceMetrics)
def performance_endpoint():
    start = time.time()
    memory = psutil.Process().memory_info().rss / 1024 / 1024
    threads = threading.active_count()
    end = time.time()
    return PerformanceMetrics(
        memory_usage_mb=memory,
        execution_time_ms=(end - start) * 1000,
        threads=threads
    )