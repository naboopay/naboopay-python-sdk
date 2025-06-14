from typing import Union

import aiohttp
import requests
from tenacity import (retry, retry_if_exception_type, stop_after_attempt,
                      wait_random_exponential)

from naboopay.config.settings_api import Settings
from naboopay.src.auth.auth import Auth
from naboopay.src.services import (Account, AsyncAccount, AsyncCashout,
                                   AsyncTransaction, Cashout, Transaction)
from naboopay.utils.errors import api_exception, general_exception


class NabooPay:
    def __init__(
        self,
        token: Union[str, None] = None,
        base_url: Union[str, None] = None,
    ):
        self._settings = None
        if base_url is None:
            self._settings = Settings().model_dump()
            self.base_url = self._settings["base_url"]
        else:
            self.base_url = self.base_url
        if token is None:
            self._settings = Settings().model_dump()
            self.auth = Auth(self.settings["naboo_api_key"])
        else:
            self.auth = Auth(token)

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
    def __init__(
        self, token: Union[str, None] = None, base_url: Union[str, None] = None
    ):
        self.settings = None
        if base_url is None:
            self.settings = Settings().model_dump()
            self.base_url = self.settings["base_url"]
        else:
            self.base_url = self.base_url

        if token is None:
            self.settings = Settings().model_dump()
            self.auth = Auth(self.settings["naboo_api_key"])
        else:
            self.auth = Auth(token)

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
