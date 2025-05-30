# NabooPay Python SDK Workshop

Hey there! Welcome to this fun and practical workshop on using the NabooPay Python SDK. Whether you're syncing up synchronously or diving into async adventures, this guide has got you covered. We'll walk through installing the SDK, setting up clients, and performing some cool operations like retrieving account details, managing transactions, and handling cashouts. I’ve added a sprinkle of humor to keep things light because who said coding can’t be fun, right? Let’s dive in!

## Table of Contents

1. [Installation](#installation)
2. [Client Initialization](#client-initialization)
   - 2.1 [Token Loading](#token-loading)
   - 2.2 [Synchronous Client](#synchronous-client)
   - 2.3 [Asynchronous Client](#asynchronous-client)
3. [Operations](#operations)
   - 3.1 [Retrieve Account Details](#retrieve-account-details)
     - 3.1.1 [Synchronous](#synchronous)
     - 3.1.2 [Asynchronous](#asynchronous)
   - 3.2 [Transactions](#transactions)
     - 3.2.1 [Create Transaction](#create-transaction)
       - 3.2.1.1 [Synchronous](#synchronous-1)
       - 3.2.1.2 [Asynchronous](#asynchronous-1)
     - 3.2.2 [Delete Transaction](#delete-transaction)
       - 3.2.2.1 [Synchronous](#synchronous-2)
       - 3.2.2.2 [Asynchronous](#asynchronous-2)
     - 3.2.3 [Get Transactions](#get-transactions)
       - 3.2.3.1 [Synchronous](#synchronous-3)
       - 3.2.3.2 [Asynchronous](#asynchronous-3)
   - 3.3 [Cashout](#cashout)
     - 3.3.1 [Cashout with Wave](#cashout-with-wave)
       - 3.3.1.1 [Synchronous](#synchronous-4)
       - 3.3.1.2 [Asynchronous](#asynchronous-4)
     - 3.3.2 [Cashout with Orange Money](#cashout-with-orange-money)
       - 3.3.2.1 [Synchronous](#synchronous-5)
       - 3.3.2.2 [Asynchronous](#asynchronous-5)

---

## Installation

Let’s kick things off by installing the NabooPay Python SDK with this magical command. Run it in your terminal, and you’re good to go!

```bash
pip install git+https://github.com/naboopay/naboopay-python-sdk.git
```

---

## Client Initialization

Before we can do anything fancy, we need to set up our clients. This involves loading our API token and initializing both synchronous and asynchronous clients. Here’s how:

### Token Loading

First, grab your API token from a `.env` file—it’s the safest way to keep your secrets, well, secret! If you don’t have one yet, head to the NabooPay dashboard and conjure one up.

```python
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ.get("NABOOPAY_API_KEY")
# Alternatively: token = "your_token_here" (but shh, that’s not safe!)

# You wanna know my phone number 😂, no bro you can't 🙃 let's load them as env var
phone_number_1 = os.environ.get("TEST_NUMBER_1")
phone_number_2 = os.environ.get("TEST_NUMBER_2")
```

### Synchronous Client

For those who like to take things one step at a time, here’s how to set up the synchronous client:

```python
from naboopay import NabooPay

naboopay_client = NabooPay(token=token)
```

### Asynchronous Client

If you’re ready to live on the async edge, initialize the asynchronous client like this:

```python
from naboopay import NabooPayAsync

naboopay_async_client = NabooPayAsync(token=token)
```

---

## Operations

Now for the fun part let’s do stuff with the NabooPay API! We’ll cover retrieving account details, managing transactions, and cashing out, with examples for both synchronous and asynchronous approaches.

### Retrieve Account Details

Let’s peek at your account info.

#### Synchronous

Simple and straightforward get your account details and print them:

```python
account_info_sync = naboopay_client.account.get_info()
print(account_info_sync)
```

#### Asynchronous

For the async fans, here’s how to fetch account details. Don’t forget to run it with `asyncio`:

```python
import asyncio

async def account_test():
    account_info_async = await naboopay_async_client.account.get_info()
    print(account_info_async)

asyncio.run(account_test())
```

---

### Transactions

Time to play with transactions, create them, delete them, and fetch them!

#### Create Transaction

Let’s whip up a transaction with some payment methods and a snazzy T-shirt product. Feel free to add more items (maybe a “Unicorn Horn”?) as long as it’s legal!

```python
from naboopay.models import TransactionRequest, ProductModel, Wallet

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
        # Add more products here if you’re feeling fancy!
    ],
)
```

##### Synchronous

Create that transaction and see what you get:

```python
from naboopay.models import TransactionResponse

response_sync: TransactionResponse = naboopay_client.transaction.create(request=request)
print(response_sync)
```

##### Asynchronous

Async creation because why wait around?

```python
async def create_transaction_async():
    response_async: TransactionResponse = await naboopay_async_client.transaction.create(request=request)
    print(response_async)
    return response_async

response_async = asyncio.run(create_transaction_async())
```

#### Delete Transaction

Got a transaction you don’t like? Let’s delete it using the `order_id` from the creation step.

##### Synchronous

Using the `response_sync` from above:

```python
from naboopay.models import DeleteTransactionRequest

request_sync_delete = DeleteTransactionRequest(order_id=response_sync.order_id)
response_sync_delete = naboopay_client.transaction.delete(request=request_sync_delete)
print(response_sync_delete)
```

##### Asynchronous

Using the `response_async` from the async creation:

```python
request_async_delete = DeleteTransactionRequest(order_id=response_async.order_id)

async def delete_transaction_async():
    response_async_delete = await naboopay_async_client.transaction.delete(request=request_async_delete)
    print(response_async_delete)

asyncio.run(delete_transaction_async())
```

#### Get Transactions

Want to see all your transactions or just one? Here’s how:

##### Synchronous

Fetch all transactions:

```python
all_transactions_sync = naboopay_client.transaction.get_all()
print(all_transactions_sync)
```

Grab a single transaction using an `order_id` (we’ll use the first one from the list):

```python
transaction_id = all_transactions_sync.transactions[0].order_id
one_transaction_sync = naboopay_client.transaction.get_one(order_id=transaction_id)
print(one_transaction_sync)
```

##### Asynchronous

All transactions, async style:

```python
async def get_all_transactions_async():
    all_transactions_async = await naboopay_async_client.transaction.get_all()
    print(all_transactions_async)

asyncio.run(get_all_transactions_async())
```

One transaction, async style:

```python
async def get_one_transaction_async():
    one_transaction_async = await naboopay_async_client.transaction.get_one(order_id=transaction_id)
    print(one_transaction_async)

asyncio.run(get_one_transaction_async())
```

---

### Cashout

Let’s move some money with Wave and Orange Money. Pro tip: use your own phone number for testing unless you want to surprise sudoping01!

#### Cashout with Wave

Set up your cashout request:

```python
from naboopay.models import CashOutRequest

request_wave: CashOutRequest = CashOutRequest(
    full_name="sudoping01",
    amount=10000,
    phone_number=phone_number_1,  # Don’t change this unless you’re testing sudoping01 likes it this way! 😂
)
```

##### Synchronous

Cash out and handle any hiccups:

```python
try:
    response_wave_sync = naboopay_client.cashout.wave(request=request_wave)
    print(response_wave_sync)
except Exception as e:
    print(f"Exception: {e}")
```

##### Asynchronous

Async cashout with error handling:

```python
async def cashout_wave_async():
    try:
        response_wave_async = await naboopay_async_client.cashout.wave(request=request_wave)
        print(response_wave_async)
    except Exception as e:
        print(f"Exception: {e}")

asyncio.run(cashout_wave_async())
```

#### Cashout with Orange Money

Another cashout, this time with Orange Money:

```python
request_orange: CashOutRequest = CashOutRequest(
    full_name="Djim Patrick Lo",  # Hi Patrick! 😂
    amount=100,
    phone_number=phone_number_2,  # Swap this out for testing, or Patrick might cash in!
)
```

##### Synchronous

```python
try:
    response_orange_sync = naboopay_client.cashout.orange_money(request=request_orange)
    print(response_orange_sync)
except Exception as e:
    print(f"Exception: {e}")
```

##### Asynchronous

```python
async def cashout_orange_async():
    try:
        response_orange_async = await naboopay_async_client.cashout.orange_money(request=request_orange)
        print(response_orange_async)
    except Exception as e:
        print(f"Exception: {e}")

asyncio.run(cashout_orange_async())
```

---

## Wrapping Up

And there you have it a full workshop on using the NabooPay Python SDK! You’ve installed it, set up clients, and mastered account details, transactions, and cashouts both synchronously and asynchronously. Pretty cool, right? Feel free to tweak the code, explore more features, and keep the good vibes going. Good Integration 🫂!
