"""Avanza library."""
import logging
import re
from http.client import responses

import requests

logger = logging.getLogger(__name__)


class AvanzaError(Exception):
    """Avanza error."""

    pass


class Avanza:
    """Avanza class."""

    BASE_URL = "https://avanza.se"

    def __init__(self, headers, cookies):
        """Setup."""
        self.headers = headers
        self.cookies = cookies

    def get_account_values(self):
        """Return total values for all accounts."""
        req = requests.get(
            self.BASE_URL + "/_cqbe/ff/overview/categorizedAccounts",
            headers=self.headers,
            cookies=self.cookies,
        )

        if req.status_code != 200:
            raise AvanzaError(
                f"HTTP request failed status code {req.status_code}"
                f" ({responses[req.status_code]}) ({req.text})"
            )

        account_values = {}
        for account in req.json()["accounts"]:
            account_key = re.sub(
                "[^0-9a-zA-Z]+", "-", account["name"]["userDefinedName"]
            ).lower()
            account_values[account_key] = account["totalValue"]["value"]

        return account_values
