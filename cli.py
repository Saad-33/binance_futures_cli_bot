import argparse
import logging
import sys

from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    ValidationError,
)
from bot.logging_config import setup_logging


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    return parser.parse_args()


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        args = parse_arguments()

        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        print("\n---------------------------------")
        print("Order Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")
        print("---------------------------------\n")

        confirm = input("Confirm order execution? (y/n): ")
        if confirm.lower() != "y":
            print("Order cancelled.")
            return

        client = BinanceFuturesClient()
        service = OrderService(client)

        result = service.execute_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\nOrder Result")
        print(f"Order ID: {result.order_id}")
        print(f"Status: {result.status}")
        print(f"Executed Quantity: {result.executed_qty}")
        print(f"Average Price: {result.avg_price}")
        print("Order executed successfully.")

    except ValidationError as ve:
        print(f"Validation Error: {ve}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
        sys.exit(1)
    except Exception as e:
        logger.exception("Fatal error occurred.")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
