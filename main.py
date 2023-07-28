from prefect import flow, get_run_logger
from utils import get_valuation, upload_valuation


@flow(name="Update 3CommaDigital Wallets")
def update_valuation(wallet: str = "3C2", date: str = "2023-07-28"):
    logger = get_run_logger()
    valuation = get_valuation(wallet, date)
    if valuation:
        logger.info(valuation)
        upload_valuation(valuation)


if __name__ == "__main__":
    update_valuation()
