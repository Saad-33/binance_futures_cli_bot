import logging
import random
import time
from typing import Any, Dict

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from .config import Settings

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    """
    Binance Futures Client.

    Supports:
    - Real Binance Testnet execution
    - TEST_MODE simulated execution
    """

    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self) -> None:
        self.test_mode: bool = Settings.TEST_MODE

        if not self.test_mode:
            if not Settings.API_KEY or not Settings.API_SECRET:
                raise EnvironmentError(
                    "API credentials not set in environment variables."
                )

            self.client = Client(Settings.API_KEY, Settings.API_SECRET)
            self.client.FUTURES_URL = self.BASE_URL
        else:
            logger.info("Running in TEST_MODE (simulated execution).")

    def place_order(self, **params: Any) -> Dict[str, Any]:
        """
        Place a futures order (real or simulated).
        """

        logger.info("Sending order request: %s", params)

        if self.test_mode:
            # Simulate realistic network latency
            time.sleep(1)

            order_type = params.get("type", "MARKET")

            simulated_response = {
                "orderId": random.randint(10_000_000, 99_999_999),
                "status": "FILLED" if order_type == "MARKET" else "NEW",
                "executedQty": (
                    str(params["quantity"]) if order_type == "MARKET" else "0"
                ),
                "avgPrice": (
                    str(params.get("price", 59874.23))
                    if order_type == "MARKET"
                    else "0"
                ),
            }

            logger.info("Simulated response: %s", simulated_response)
            return simulated_response

        try:
            response = self.client.futures_create_order(**params)
            logger.info("Received response: %s", response)
            return response

        except (BinanceAPIException, BinanceRequestException):
            logger.exception("Binance API error occurred.")
            raise

        except Exception:
            logger.exception("Unexpected error while placing order.")
            raise
