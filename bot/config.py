import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TEST_MODE: bool = os.getenv("TEST_MODE", "false").lower() == "true"
    API_KEY: str | None = os.getenv("BINANCE_API_KEY")
    API_SECRET: str | None = os.getenv("BINANCE_API_SECRET")
