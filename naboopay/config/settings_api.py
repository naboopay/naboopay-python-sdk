from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_url: str = Field(
        validation_alias="BASE_URL", default="https://api.naboopay.com/api/v1"
    )
    naboo_api_key: str = Field(validation_alias="NABOO_API_KEY")
