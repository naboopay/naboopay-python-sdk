import hashlib
import hmac
import json
import os
from typing import Union

from naboopay.models import WebhookModel


class Webhook:
    def __init__(self,webhook_secret_key = os.getenv("NABOOPAY_WEBHOOK_SECRET")):
        self._secret_key = webhook_secret_key
        pass

    def verify(self,payload:dict,signature:str) -> Union[WebhookModel,None]:
        payload_bytes = json.dumps(payload).encode()
        expected_signature = hmac.new(self._secret_key.encode(), payload_bytes, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_signature):
            return None 
        return WebhookModel(**payload)
