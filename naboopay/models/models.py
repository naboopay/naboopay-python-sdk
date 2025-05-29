from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..config.settings import BASE_URL
from ..utils.exceptions import APIError, AuthenticationError, NabooPayError


class Wallet(str, Enum):
    WAVE = "WAVE"
    ORANGE_MONEY = "ORANGE_MONEY"
    FREE_MONEY = "FREE_MONEY"
    BANK = "BANK"


class TransactionStatusEnum(str, Enum):
    pending = "pending"
    paid = "paid"
    done = "done"
    part_paid = "part_paid"


class ProductModel(BaseModel):
    name: str
    category: str
    amount: int
    quantity: int
    description: str


@dataclass
class httpsRequestInformation:
    endpoint: str
    method: str


class NabooRequest:
    create_transaction: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/transaction/create-transaction", method="POST"
    )

    delete_transaction: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/transaction/delete-transaction", method="DELETE"
    )

    get_one_transaction: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/transaction/get-one-transaction", method="GET"
    )

    get_transaction: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/transaction/get-transactions", method="GET"
    )

    cashout_orange_money: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/cashout/orange-money", method="POST"
    )

    cashout_wave: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/cashout/wave", method="POST"
    )

    account: httpsRequestInformation = httpsRequestInformation(
        endpoint=f"{BASE_URL}/account/", method="GET"
    )


class TransactionRequest(BaseModel):
    method_of_payment: List[Wallet]
    products: Optional[List[ProductModel]] = None
    success_url: Optional[str] = Field(
        default="https://checkout.naboopay.com/success", pattern=r"^https:\/\/[^\s]+$"
    )
    error_url: Optional[str] = Field(
        default="https://checkout.naboopay.com/error", pattern=r"^https:\/\/[^\s]+$"
    )
    fees_customer_side: Optional[bool] = True
    is_escrow: bool = False
    is_merchant: bool = False


class TransactionResponse(BaseModel):
    order_id: str
    method_of_payment: List[str]
    amount: int = 0
    amount_to_pay: int = 0
    currency: str
    created_at: datetime
    transaction_status: str = "pending"
    is_escrow: bool = False
    is_merchant: bool = False
    checkout_url: str


class DeleteTransactionRequest(BaseModel):
    order_id: str


class DeleteTransactionResponse(BaseModel):
    order_id: str
    message: str


class GetOneTransaction(BaseModel):
    order_id: str
    method_of_payment: List[Wallet]
    amount: int
    amount_to_pay: int
    currency: str
    created_at: datetime
    transaction_status: TransactionStatusEnum
    products: Optional[List[ProductModel]] = None
    is_done: bool
    is_escrow: bool
    is_merchant: bool
    checkout_url: str


class GetAllTransaction(BaseModel):
    transactions: List[GetOneTransaction]


class GetAccountResponse(BaseModel):
    account_number: str
    balance: float
    account_is_activate: bool
    method_of_payment: Wallet
    loyalty_credit: int


class CashOutRequest(BaseModel):
    full_name: str
    amount: int
    phone_number: str


class CashOutResponse(BaseModel):
    phone_number: str
    amount: int
    full_name: str
    status: TransactionStatusEnum


class ExceptionMessage:
    messages: Dict[int, str] = {
        401: "Invalid or expired token",
        403: "Forbidden: You do not have permission to access this resource",
        404: "Resource not found",
    }

    default: str = ("API error {}",)
    failed: str = "Request failed: {}"


class CodeStatusExceptions:
    exceptions: Dict[int, Any] = {
        401: AuthenticationError,
        403: APIError,
        404: APIError,
    }

    default = NabooPayError
