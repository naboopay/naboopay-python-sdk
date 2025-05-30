import asyncio
import os

from dotenv import load_dotenv

from naboopay import NabooPay, NabooPayAsync
from naboopay.models import CashOutRequest  # GetOneTransaction
from naboopay.models import (DeleteTransactionRequest, ProductModel,
                             TransactionRequest, TransactionResponse, Wallet)

# Load environment variables from .env file
load_dotenv()
token = os.environ.get("NABOOPAY_API_KEY")

number_1 = os.environ.get("TEST_NUMBER_1")
number_2 = os.environ.get("TEST_NUMBER_2")

# Initialize synchronous and asynchronous clients with the API token
naboopay_client = NabooPay(token=token)
naboopay_async_client = NabooPayAsync(token=token)

# ================================================
#                  Retrieve account details
# ================================================

#               |==================|
#               |    Synchronous   |
#               |==================|

account_info_sync = naboopay_client.account.get_info()
print(account_info_sync)

#               |==================|
#               |   Asynchronous   |
#               |==================|


async def account_test():
    account_info_async = await naboopay_async_client.account.get_info()
    print(account_info_async)


asyncio.run(account_test())

# ================================================
#                  Transactions
# ================================================

# --------------------|
# Create Transaction  |
# --------------------|


# Prepare a transaction request with multiple payment methods and a product
request = TransactionRequest(
    method_of_payment=[Wallet.WAVE, Wallet.ORANGE_MONEY, Wallet.FREE_MONEY],
    products=[
        ProductModel(
            name="T-shirt",
            category="clothing",
            amount=10000,
            quantity=1,
            description="test description",
        ),
        # You can add many product (same way then the T-shirt product: ProductModel(.........))
    ],
)

#               |==================|
#               |   Synchronous    |
#               |==================|

response_sync: TransactionResponse = naboopay_client.transaction.create(request=request)
print(response_sync)

#               |==================|
#               |   Asynchronous   |
#               |==================|


async def create_transaction_async():
    response_async: TransactionResponse = (
        await naboopay_async_client.transaction.create(request=request)
    )
    print(response_async)
    return response_async


response_async = asyncio.run(create_transaction_async())

# ------------------------------
# Delete Transaction
# ------------------------------


# Prepare delete request for created transaction
request_sync_delete = DeleteTransactionRequest(order_id=response_sync.order_id)


response_sync_delete = naboopay_client.transaction.delete(request=request_sync_delete)
print(response_sync_delete)

#  (we just delete the response_syn.order_id so we have to use an other transaction let's use response_asyn.order_id transaction)
request_async_delete = DeleteTransactionRequest(order_id=response_async.order_id)


async def delete_transaction_async():
    response_async_delete = await naboopay_async_client.transaction.delete(
        request=request_async_delete
    )
    print(response_async_delete)


asyncio.run(delete_transaction_async())

# ------------------------------
# Get Transactions
# ------------------------------

# Retrieve all transactions

# default param
#    limit: int = 50,
#    amount: int | None = None,                    #filter
#    transaction_status: str | None = None,        #filter
#    created_at_start: str | None = None,          #filter
#    created_at_end: str | None = None             #filter


#               |==================|
#               |   Synchronous    |
#               |==================|


all_transactions_sync = naboopay_client.transaction.get_all()
print(all_transactions_sync)


#               |==================|
#               |   Asynchronous   |
#               |==================|


async def get_all_transactions_async():
    all_transactions_async = await naboopay_async_client.transaction.get_all()
    print(all_transactions_async)


asyncio.run(get_all_transactions_async())

# Get One Transaction: Retrieve a single transaction

# We need the transaction id,  let's use the first transaction's ID from the list we got from all transaction

transaction_id = all_transactions_sync.transactions[0].order_id


#               |==================|
#               |    Synchronous   |
#               |==================|


one_transaction_sync = naboopay_client.transaction.get_one(order_id=transaction_id)
print(one_transaction_sync)

#               |==================|
#               |   Asynchronous   |
#               |==================|


async def get_one_transaction_async():
    one_transaction_async = await naboopay_async_client.transaction.get_one(
        order_id=transaction_id
    )
    print(one_transaction_async)


asyncio.run(get_one_transaction_async())

# ================================================
#               Cashout
# ================================================


# ------------------------------
# Cashout with Wave
# ------------------------------

request_wave: CashOutRequest = CashOutRequest(
    full_name="sudoping01",
    amount=10000,
    phone_number=number_1,  # please when testing don't change this number 😂
)


#               |==================|
#               |    Synchronous   |
#               |==================|

# Actually the api is blocking (the client) when doing multiple cash simultaniously (so let's handle exception then)
try:
    response_wave_sync = naboopay_client.cashout.wave(request=request_wave)
    print(response_wave_sync)
except Exception as e:
    print(f"Exception: {e}")


#               |==================|
#               |    Asynchronous  |
#               |==================|


async def cashout_wave_async():
    try:
        response_wave_async = await naboopay_async_client.cashout.wave(
            request=request_wave
        )
        print(response_wave_async)
    except Exception as e:
        print(f"Exception: {e}")


asyncio.run(cashout_wave_async())

# ------------------------------
# Cashout with Orange Money
# ------------------------------

request_orange: CashOutRequest = CashOutRequest(
    full_name="Djim Patrick Lo",  # 😂 Patrick
    amount=100,
    phone_number=number_2,  # please don't forget to change this num to the first one 😂
)

#               |==================|
#               |    Synchronous  |
#               |==================|


try:
    response_orange_sync = naboopay_client.cashout.orange_money(request=request_orange)
    print(response_orange_sync)
except Exception as e:
    print(f"Excetion: {e}")


#               |==================|
#               |    Asynchronous  |
#               |==================|


async def cashout_orange_async():
    try:
        response_orange_async = await naboopay_async_client.cashout.orange_money(
            request=request_orange
        )
        print(response_orange_async)
    except Exception as e:
        print(f"Exception: {e}")


asyncio.run(cashout_orange_async())
