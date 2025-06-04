import os

import aiohttp
import requests
from tenacity import (retry, retry_if_exception_type, stop_after_attempt,
                      wait_random_exponential)

from naboopay.config.settings import BASE_URL, NABOOPAY_API_KEY_ENV
from naboopay.src.auth.auth import Auth
from naboopay.src.services import (Account, AsyncAccount, AsyncCashout,
                                   AsyncTransaction, Cashout, Transaction)
from naboopay.utils.errors import api_exception, general_exception


class NabooPay:
    def __init__(
        self,
        token: str = os.environ.get(NABOOPAY_API_KEY_ENV),
        base_url: str = BASE_URL,
    ):
        self.auth = Auth(token)
        self.base_url = base_url
        self.transaction = Transaction(self)
        self.account = Account(self)
        self.cashout = Cashout(self)

    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_random_exponential(multiplier=1, max=40),
        stop=stop_after_attempt(3),
    )
    def _make_request(self, method: str, endpoint: str, **kwargs):
        headers = self.auth.get_headers()
        try:
            response = requests.request(method, endpoint, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise api_exception(code=e.response.status_code, error=e)
        except requests.exceptions.RequestException as e:
            raise general_exception(error=e)


class NabooPayAsync:
    def __init__(self, token: str = None, base_url: str = BASE_URL):
        self.auth = Auth(token) if token else Auth()
        self.base_url = base_url
        self.transaction = AsyncTransaction(self)
        self.account = AsyncAccount(self)
        self.cashout = AsyncCashout(self)

    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_random_exponential(multiplier=1, max=40),
        stop=stop_after_attempt(3),
    )
    async def _make_request(self, method: str, endpoint: str, **kwargs):
        headers = self.auth.get_headers()
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, endpoint, headers=headers, **kwargs
            ) as response:
                try:
                    response.raise_for_status()
                    return await response.json()
                except aiohttp.ClientResponseError as e:
                    raise api_exception(code=e.status, error=e)
                except aiohttp.ClientError as e:
                    raise general_exception(error=e)
