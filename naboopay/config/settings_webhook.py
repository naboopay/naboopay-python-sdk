from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    webhook_secret_key: str = Field(validation_alias="WEBHOOK_SECRET_KEY")
