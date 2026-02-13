# Binance Futures Trading Bot (Testnet)

Production-style CLI trading bot for Binance USDT-M Futures Testnet.

## Overview

This project demonstrates a clean-architecture Python trading bot capable of placing:

- MARKET orders
- LIMIT orders
- BUY / SELL support
- Structured logging
- Robust exception handling
- Input validation
- Confirmation prompt (UX enhancement)

Built with production-quality patterns:
- Layered architecture
- Separation of concerns
- API abstraction
- Dataclass response model
- Environment-based credentials

---

## Features

- Clean CLI interface (argparse)
- Structured logging to file
- Binance Futures Testnet integration
- Input validation layer
- Graceful failure handling
- Rotating log files
- Confirmation prompt before execution

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd trading_bot
