from naboopay.models import CashOutRequest, CashOutResponse, NabooRequest


class Cashout:
    def __init__(self, client):
        self.client = client

    def wave(self, request: CashOutRequest) -> CashOutResponse:
        data = request.dict()
        response = self.client._make_request(
            method=NabooRequest.cashout_wave.method,
            endpoint=NabooRequest.cashout_wave.endpoint,
            json=data,
        )
        return CashOutResponse(**response)

    def orange_money(self, request: CashOutRequest) -> CashOutResponse:
        data = request.dict()
        response = self.client._make_request(
            method=NabooRequest.cashout_orange_money.method,
            endpoint=NabooRequest.cashout_orange_money.endpoint,
            json=data,
        )
        return CashOutResponse(**response)


class AsyncCashout:
    def __init__(self, client):
        self.client = client

    async def wave(self, request: CashOutRequest) -> CashOutResponse:
        data = request.dict()
        response = await self.client._make_request(
            method=NabooRequest.cashout_wave.method,
            endpoint=NabooRequest.cashout_wave.endpoint,
            json=data,
        )
        return CashOutResponse(**response)

    async def orange_money(self, request: CashOutRequest) -> CashOutResponse:
        data = request.dict()
        response = await self.client._make_request(
            method=NabooRequest.cashout_orange_money.method,
            endpoint=NabooRequest.cashout_orange_money.endpoint,
            json=data,
        )
        return CashOutResponse(**response)
