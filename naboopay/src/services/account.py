from naboopay.models import GetAccountResponse, NabooRequest


class Account:
    def __init__(self, client):
        self.client = client

    def get_info(self) -> GetAccountResponse:
        response = self.client._make_request(
            method=NabooRequest.account.method, endpoint=NabooRequest.account.endpoint
        )
        return GetAccountResponse(**response)


class AsyncAccount:
    def __init__(self, client):
        self.client = client

    async def get_info(self) -> GetAccountResponse:
        response = await self.client._make_request(
            method=NabooRequest.account.method, endpoint=NabooRequest.account.endpoint
        )
        return GetAccountResponse(**response)
