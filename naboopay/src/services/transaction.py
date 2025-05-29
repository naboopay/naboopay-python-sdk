from typing import Optional

from naboopay.models import (DeleteTransactionRequest,
                             DeleteTransactionResponse, GetAllTransaction,
                             GetOneTransaction, NabooRequest,
                             TransactionRequest, TransactionResponse)


class Transaction:
    def __init__(self, client):
        self.client = client

    def create(self, request: TransactionRequest) -> TransactionResponse:
        data = request.dict(exclude_unset=True)
        response = self.client._make_request(
            method=NabooRequest.create_transaction.method,
            endpoint=NabooRequest.create_transaction.endpoint,
            json=data,
        )
        return TransactionResponse(**response)

    def delete(self, request: DeleteTransactionRequest) -> DeleteTransactionResponse:
        data = request.dict()
        response = self.client._make_request(
            method=NabooRequest.delete_transaction.method,
            endpoint=NabooRequest.delete_transaction.endpoint,
            json=data,
        )
        return DeleteTransactionResponse(**response)

    def get_all(
        self,
        limit: int = 50,
        amount: Optional[int] = None,
        transaction_status: Optional[str] = None,
        created_at_start: Optional[str] = None,
        created_at_end: Optional[str] = None,
    ) -> GetAllTransaction:
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "amount": amount,
                "transaction_status": transaction_status,
                "created_at_start": created_at_start,
                "created_at_end": created_at_end,
            }.items()
            if v is not None
        }
        response = self.client._make_request(
            method=NabooRequest.get_transaction.method,
            endpoint=NabooRequest.get_transaction.endpoint,
            params=params,
        )
        return GetAllTransaction(**response)

    def get_one(self, order_id: str) -> GetOneTransaction:
        params = {"order_id": order_id}
        response = self.client._make_request(
            method=NabooRequest.get_one_transaction.method,
            endpoint=NabooRequest.get_one_transaction.endpoint,
            params=params,
        )
        return GetOneTransaction(**response)


class AsyncTransaction:
    def __init__(self, client):
        self.client = client

    async def create(self, request: TransactionRequest) -> TransactionResponse:
        data = request.dict(exclude_unset=True)
        response = await self.client._make_request(
            method=NabooRequest.create_transaction.method,
            endpoint=NabooRequest.create_transaction.endpoint,
            json=data,
        )
        return TransactionResponse(**response)

    async def delete(
        self, request: DeleteTransactionRequest
    ) -> DeleteTransactionResponse:
        data = request.dict()
        response = await self.client._make_request(
            method=NabooRequest.delete_transaction.method,
            endpoint=NabooRequest.delete_transaction.endpoint,
            json=data,
        )
        return DeleteTransactionResponse(**response)

    async def get_all(
        self,
        limit: int = 50,
        amount: Optional[int] = None,
        transaction_status: Optional[str] = None,
        created_at_start: Optional[str] = None,
        created_at_end: Optional[str] = None,
    ) -> GetAllTransaction:
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "amount": amount,
                "transaction_status": transaction_status,
                "created_at_start": created_at_start,
                "created_at_end": created_at_end,
            }.items()
            if v is not None
        }
        response = await self.client._make_request(
            method=NabooRequest.get_transaction.method,
            endpoint=NabooRequest.get_transaction.endpoint,
            params=params,
        )
        return GetAllTransaction(**response)

    async def get_one(self, order_id: str) -> GetOneTransaction:
        params = {"order_id": order_id}
        response = await self.client._make_request(
            method=NabooRequest.get_one_transaction.method,
            endpoint=NabooRequest.get_one_transaction.endpoint,
            params=params,
        )
        return GetOneTransaction(**response)
