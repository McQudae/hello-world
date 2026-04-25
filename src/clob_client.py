# src/clob_client.py
from typing import Any, Dict
import requests

from .config import CLOB_BASE_URL, DEFAULT_TIMEOUT


class ClobClient:
    def __init__(self, base_url: str = CLOB_BASE_URL, timeout: int = DEFAULT_TIMEOUT) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get_order_book(self, token_id: str) -> Dict[str, Any]:
        """
        Fetch the public order book for a given outcome token.

        Docs show:
          GET /order-book/{token_id}
        returning bids, asks, spread, midpoint, etc.
        """
        url = f"{self.base_url}/order-book/{token_id}"
        resp = requests.get(url, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def get_last_trade_price(self, token_id: str) -> Dict[str, Any]:
        """
        Fetch the last trade price for a given outcome token.

        Docs show:
          GET /last-trade-price?token_id=...
        returning { "price": "...", "side": "BUY"|"SELL" }.
        """
        url = f"{self.base_url}/last-trade-price"
        params = {"token_id": token_id}
        resp = requests.get(url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()