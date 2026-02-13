import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any

from .client import BinanceFuturesClient


logger = logging.getLogger(__name__)


@dataclass
class OrderResponse:
    order_id: int
    status: str
    executed_qty: float
    avg_price: Optional[float]


class OrderService:
    """
    Business logic layer for order management.
    """

    def __init__(self, client: BinanceFuturesClient) -> None:
        self.client = client

    def execute_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
    ) -> OrderResponse:

        params: Dict[str, Any] = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params.update(
                {
                    "price": price,
                    "timeInForce": "GTC",
                }
            )

        response = self.client.place_order(**params)

        return OrderResponse(
            order_id=response["orderId"],
            status=response["status"],
            executed_qty=float(response.get("executedQty", 0)),
            avg_price=float(response.get("avgPrice", 0))
            if response.get("avgPrice")
            else None,
        )
