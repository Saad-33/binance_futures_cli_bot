Binance Futures Trading Bot (Testnet)

Production-style CLI trading bot for Binance USDT-M Futures Testnet with clean architecture, structured logging, and simulation support.

Overview

This project demonstrates a production-oriented Python trading bot capable of placing:

MARKET orders

LIMIT orders

BUY / SELL orders

Structured logging of requests and responses

Robust exception handling

Input validation layer

Confirmation prompt before execution

The application follows clean architecture principles:

Layered design (CLI → Orders → Client)

Separation of concerns

API abstraction

Environment-based configuration

Structured response modeling

Simulation mode for safe execution

Features

Clean CLI interface using argparse

Input validation (symbol, side, type, quantity, price)

Structured logging to file (trading_bot.log)

Binance Futures Testnet integration

TEST_MODE simulation support

Graceful error handling

Confirmation prompt before order execution

Rotating log file configuration

Project Structure
trading_bot/
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── bot/
    ├── client.py
    ├── config.py
    ├── logging_config.py
    ├── orders.py
    └── validators.py

Architecture Flow
CLI → OrderService → BinanceFuturesClient → Binance API


The CLI never directly interacts with the API client, ensuring proper separation of concerns.

Installation
1. Clone the Repository
git clone <repo-url>
cd trading_bot

2. Create Virtual Environment
python -m venv venv


Activate on Windows:

venv\Scripts\activate


Activate on macOS/Linux:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

Environment Configuration

Create a .env file in the project root:

BINANCE_API_KEY=dummy
BINANCE_API_SECRET=dummy
TEST_MODE=true

TEST_MODE

TEST_MODE=true → Simulated execution (safe, no real API calls)

TEST_MODE=false → Connects to Binance Futures Testnet (requires valid API keys)

Simulation mode is enabled by default for safe evaluation.

Usage
MARKET Order Example
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

LIMIT Order Example
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 61000

Example Output
========================================
Order Summary
========================================
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01
========================================

Confirm order execution? (y/n): y

Order Result
Order ID: 35869492
Status: FILLED
Executed Quantity: 0.01
Average Price: 59874.23
Order executed successfully.

Logging

All order requests, responses, and errors are logged to:

trading_bot.log


Log entries include:

Timestamp

Log level

Module name

Request payload

Response payload

Full stack traces for errors

Example log snippet:

2026-02-13 15:22:52,121 | INFO | bot.client | Running in TEST_MODE (simulated execution).
2026-02-13 15:22:52,122 | INFO | bot.client | Sending order request: {...}
2026-02-13 15:22:53,123 | INFO | bot.client | Simulated response: {...}

Validation Rules

The application validates:

Invalid symbol format

Invalid side (BUY/SELL)

Invalid order type (MARKET/LIMIT)

Missing price for LIMIT orders

Negative or zero quantity

Validation errors exit gracefully with a clear message.

Assumptions

TEST_MODE is enabled by default for safe evaluation.

Symbol format assumes USDT-M futures (e.g., BTCUSDT).

LIMIT orders in simulation mode return status NEW.

MARKET orders in simulation mode return status FILLED.

Leverage configuration is not included in this simplified implementation.

Error Handling

The application handles:

Binance API errors

Network errors

JSON parsing issues

Invalid user input

KeyboardInterrupt (Ctrl+C)

Unexpected runtime errors

All errors are logged with stack traces.

Future Improvements

Stop-Limit order support

Leverage and margin configuration

Position tracking module

Asynchronous execution layer

Unit and integration test suite

Docker containerization

CI/CD pipeline

Configurable logging levels

Risk management module

Technical Stack

Python 3.x

python-binance

python-dotenv

argparse

logging

Submission Notes

This project is intentionally designed to:

Demonstrate clean architecture

Showcase API abstraction

Emphasize production-style logging

Ensure safe execution via simulation mode

Be runnable immediately by evaluators

No real API keys are required when running in TEST_MODE.
