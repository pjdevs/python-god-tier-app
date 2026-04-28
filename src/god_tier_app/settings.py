from pydantic_settings import BaseSettings, SettingsConfigDict


class GodTierSettings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_prefix="GOD_TIER_")

    hello_message: str
