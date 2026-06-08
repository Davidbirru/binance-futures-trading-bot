import typer
import logging

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type
)

from bot.logging_config import (
    setup_logger
)

app = typer.Typer()


@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    setup_logger()

    try:

        side = validate_side(side)
        order_type = validate_order_type(order_type)

        print("\nORDER REQUEST")
        print("=" * 40)

        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if order_type == "LIMIT":

            if price is None:
                raise ValueError(
                    "Price required for LIMIT order"
                )

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        else:

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        print("\nORDER RESPONSE")
        print("=" * 40)

        print(
            f"Order ID: "
            f"{response.get('orderId')}"
        )

        print(
            f"Status: "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty: "
            f"{response.get('executedQty')}"
        )

        print("\nSUCCESS")

    except Exception as e:

        logging.error(str(e))
        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    app()