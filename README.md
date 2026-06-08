# Binance Futures Testnet Trading Bot

## Overview

A Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* Input validation
* Structured project architecture
* API request/response logging
* Exception handling
* Environment variable based credential management

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── cli.py
├── README.md
├── requirements.txt
└── .env

## Installation

```bash
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Usage

### MARKET Order

```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

### LIMIT Order

```bash
python cli.py BTCUSDT SELL LIMIT 0.001 --price 100000
```

## Logging

Logs are stored in:

```text
logs/trading.log
```

## Assumptions

* Binance Futures Testnet account is active.
* Valid API credentials are configured.
* User has testnet balance available.
