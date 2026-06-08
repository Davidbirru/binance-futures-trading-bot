from bot.client import client
import logging


def place_market_order(symbol, side, quantity):

    logging.info(
        f"REQUEST: MARKET {side} {quantity} {symbol}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(
        f"RESPONSE: {response}"
    )

    return response


def place_limit_order(
    symbol,
    side,
    quantity,
    price
):

    logging.info(
        f"REQUEST: LIMIT {side} {quantity} {symbol} @ {price}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logging.info(
        f"RESPONSE: {response}"
    )

    return response