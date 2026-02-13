import re


class ValidationError(Exception):
    """Custom validation exception."""


def validate_symbol(symbol: str) -> None:
    if not re.match(r"^[A-Z0-9]{6,20}$", symbol):
        raise ValidationError("Invalid symbol format.")


def validate_side(side: str) -> None:
    if side not in {"BUY", "SELL"}:
        raise ValidationError("Side must be BUY or SELL.")


def validate_order_type(order_type: str) -> None:
    if order_type not in {"MARKET", "LIMIT"}:
        raise ValidationError("Order type must be MARKET or LIMIT.")


def validate_quantity(quantity: float) -> None:
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")


def validate_price(order_type: str, price: float | None) -> None:
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValidationError("LIMIT orders require a positive price.")
