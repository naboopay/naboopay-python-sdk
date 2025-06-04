NabooPay Python SDK API Documentation
This document provides detailed information on how to use the NabooPay Python SDK, including installation, client initialization, and available operations for accounts, transactions, cashouts, and webhooks.
Table of Contents

Installation
Client Initialization
Synchronous Client
Asynchronous Client


Account Operations
Get Account Info


Transaction Operations
Create Transaction
Delete Transaction
Get All Transactions
Get One Transaction


Cashout Operations
Cashout with Wave
Cashout with Orange Money


Webhook Handling
Models
Error Handling


Installation
Install the NabooPay Python SDK directly from GitHub using pip:
pip install git+https://github.com/naboopay/naboopay-python-sdk.git

For a faster installation, use uv:
uv pip install git+https://github.com/naboopay/naboopay-python-sdk.git


Client Initialization
To interact with the NabooPay API, initialize a client with your API token. The SDK supports both synchronous and asynchronous clients.
Synchronous Client
Initialize the synchronous client using the NabooPay class:
from naboopay import NabooPay
import os

token = os.environ.get("NABOOPAY_API_KEY")
client = NabooPay(token=token)

Asynchronous Client
Initialize the asynchronous client using the NabooPayAsync class:
from naboopay import NabooPayAsync
import os

token = os.environ.get("NABOOPAY_API_KEY")
async_client = NabooPayAsync(token=token)


Account Operations
Get Account Info
Retrieve details about your NabooPay account, such as balance and activation status.
Synchronous
account_info = client.account.get_info()
print(account_info)

Asynchronous
import asyncio

async def get_account_info():
    account_info = await async_client.account.get_info()
    print(account_info)

asyncio.run(get_account_info())

Response Model: GetAccountResponse  

account_number: str  
balance: float  
account_is_activate: bool  
method_of_payment: Wallet  
loyalty_credit: int


Transaction Operations
Create Transaction
Create a new transaction with specified payment methods and products.
Synchronous
from naboopay.models import TransactionRequest, ProductModel, Wallet

request = TransactionRequest(
    method_of_payment=[Wallet.WAVE, Wallet.ORANGE_MONEY],
    products=[
        ProductModel(name="T-shirt", category="clothing", amount=10000, quantity=1, description="Test item")
    ]
)
response = client.transaction.create(request=request)
print(response)

Asynchronous
async def create_transaction():
    response = await async_client.transaction.create(request=request)
    print(response)

asyncio.run(create_transaction())

Request Model: TransactionRequest  

method_of_payment: List[Wallet]  
products: Optional[List[ProductModel]]  
success_url: Optional[str]  
error_url: Optional[str]  
fees_customer_side: Optional[bool]  
is_escrow: bool  
is_merchant: bool

Response Model: TransactionResponse  

order_id: str  
method_of_payment: List[str]  
amount: int  
amount_to_pay: int  
currency: str  
created_at: datetime  
transaction_status: str  
is_escrow: bool  
is_merchant: bool  
checkout_url: str

Delete Transaction
Delete a transaction using its order_id.
Synchronous
from naboopay.models import DeleteTransactionRequest

delete_request = DeleteTransactionRequest(order_id="your_order_id")
response = client.transaction.delete(request=delete_request)
print(response)

Asynchronous
async def delete_transaction():
    response = await async_client.transaction.delete(request=delete_request)
    print(response)

asyncio.run(delete_transaction())

Request Model: DeleteTransactionRequest  

order_id: str

Response Model: DeleteTransactionResponse  

order_id: str  
message: str

Get All Transactions
Retrieve a list of all transactions with optional filters.
Synchronous
all_transactions = client.transaction.get_all(limit=10)
print(all_transactions)

Asynchronous
async def get_all_transactions():
    all_transactions = await async_client.transaction.get_all(limit=10)
    print(all_transactions)

asyncio.run(get_all_transactions())

Parameters:  

limit: int (default: 50)  
amount: Optional[int]  
transaction_status: Optional[str]  
created_at_start: Optional[str]  
created_at_end: Optional[str]

Response Model: GetAllTransaction  

transactions: List[GetOneTransaction]

Get One Transaction
Retrieve details of a single transaction by its order_id.
Synchronous
transaction = client.transaction.get_one(order_id="your_order_id")
print(transaction)

Asynchronous
async def get_one_transaction():
    transaction = await async_client.transaction.get_one(order_id="your_order_id")
    print(transaction)

asyncio.run(get_one_transaction())

Response Model: GetOneTransaction  

order_id: str  
method_of_payment: List[Wallet]  
amount: int  
amount_to_pay: int  
currency: str  
created_at: datetime  
transaction_status: TransactionStatusEnum  
products: Optional[List[ProductModel]]  
is_done: bool  
is_escrow: bool  
is_merchant: bool  
checkout_url: str


Cashout Operations
Cashout with Wave
Perform a cashout operation using Wave.
Synchronous
from naboopay.models import CashOutRequest

cashout_request = CashOutRequest(full_name="John Doe", amount=10000, phone_number="+1234567890")
response = client.cashout.wave(request=cashout_request)
print(response)

Asynchronous
async def cashout_wave():
    response = await async_client.cashout.wave(request=cashout_request)
    print(response)

asyncio.run(cashout_wave())

Request Model: CashOutRequest  

full_name: str  
amount: int  
phone_number: str

Response Model: CashOutResponse  

phone_number: str  
amount: int  
full_name: str  
status: TransactionStatusEnum

Cashout with Orange Money
Perform a cashout operation using Orange Money.
Synchronous
response = client.cashout.orange_money(request=cashout_request)
print(response)

Asynchronous
async def cashout_orange_money():
    response = await async_client.cashout.orange_money(request=cashout_request)
    print(response)

asyncio.run(cashout_orange_money())

Request Model: CashOutRequestResponse Model: CashOutResponse  

Webhook Handling
Handle incoming webhooks to process payment events securely.
from naboopay import Webhook
import os

webhook_secret = os.environ.get("NABOOPAY_WEBHOOK_SECRET")
webhook_handler = Webhook(webhook_secret_key=webhook_secret)

# In your webhook endpoint
payload = {"order_id": "123", "amount": 10000, "transaction_status": "paid"}
signature = "some_signature"
payment = webhook_handler.verify(payload, signature)
if payment:
    print(payment.order_id)
else:
    print("Invalid signature")

Model: WebhookModel  

order_id: str  
amount: int  
currency: str  
created_at: datetime  
transaction_status: TransactionStatusEnum


Models
The SDK defines several models for requests and responses:

Wallet: Enum (WAVE, ORANGE_MONEY, FREE_MONEY, BANK)  
TransactionRequest: For creating transactions  
TransactionResponse: Response for transaction creation  
DeleteTransactionRequest: For deleting transactions  
DeleteTransactionResponse: Response for deletion  
GetOneTransaction: Details of a single transaction  
GetAllTransaction: List of transactions  
CashOutRequest: For cashout operations  
CashOutResponse: Response for cashouts  
GetAccountResponse: Account details  
WebhookModel: Webhook payload structure

For full details, see naboopay/models/models.py.

Error Handling
The SDK raises custom exceptions for various scenarios:

AuthenticationError: For 401 Unauthorized errors  
APIError: For other HTTP errors (403, 404, etc.)  
NabooPayError: General errors

Example:
try:
    response = client.transaction.create(request=request)
except AuthenticationError as e:
    print("Authentication failed:", e)
except APIError as e:
    print("API error:", e)
except NabooPayError as e:
    print("General error:", e)

