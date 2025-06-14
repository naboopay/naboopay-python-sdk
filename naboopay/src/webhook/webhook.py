import hashlib
import hmac
import json
import os
from typing import Union

from naboopay.config.settings_webhook import Settings
from naboopay.models import WebhookModel


class Webhook:
    def __init__(self,webhook_secret_key:Union[str,None] = None):
        self._settings = None
        if webhook_secret_key is None:
            self._settings = Settings().model_dump()
            self._secret_key = self._settings["webhook_secret_key"]
        else:
            self._secret_key = webhook_secret_key
        
    def verify(self,payload:dict,signature:str) -> Union[WebhookModel,None]:
        payload_bytes = json.dumps(payload).encode()
        expected_signature = hmac.new(self._secret_key.encode(), payload_bytes, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_signature):
            return None 
        return WebhookModel(**payload)
