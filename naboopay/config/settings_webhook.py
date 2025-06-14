from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    webhook_secret_key: str = Field(validation_alias='WEBHOOK_SECRET_KEY')  
