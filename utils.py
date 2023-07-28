import random
from datetime import datetime

import httpx
from prefect import flow, task

API_URL = "http://localhost:8000"


@task()
def check_if_exists(date: str, wallet: str):
    url = f"{API_URL}/valuations/{wallet}/{date}"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


@flow(name="Get valuation")
def get_valuation(date: str, wallet: str):
    """Get valuation for a wallet on a given date"""
    if not check_if_exists(date, wallet):
        return {"date": date, "wallet": wallet, "value": random.random()}
    return None


@flow(name="Upload valuation")
def upload_valuation(valuation):
    """Upload valuation for a wallet on a given date"""

    res = httpx.post(f"{API_URL}/valuations", json=valuation)
    print(res.json())
    return res.json()


if __name__ == "__main__":
    date = datetime.now().strftime("%Y-%m-%d")
    wallet = "3C2"

    valuation = {"date": date, "wallet": wallet, "value": random.random()}
    upload_valuation(valuation)
