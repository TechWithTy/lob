from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LobConfig(BaseSettings):
    # Loads from .env with prefix LOB_
    model_config = SettingsConfigDict(env_prefix="LOB_", env_file=".env", extra="ignore")

    # Required
    api_key: str = Field(..., description="Lob API key (test_... or live_...)")

    # Optional
    base_url: str = Field("https://api.lob.com/v1", description="Lob API base URL")
    api_version: Optional[str] = Field("2020-02-11", description="Lob-Version header")
    timeout: int = Field(30, description="Request timeout (seconds)")
    max_retries: int = Field(3, description="Max retries on transient errors")
    retry_delay: float = Field(1.0, description="Base delay between retries (seconds)")
    log_level: str = Field("INFO", description="Logging level")
    debug: bool = Field(False, description="Enable debug logs")
    cache_ttl: int = Field(300, description="Default cache TTL (seconds)")


config = LobConfig()

__all__ = ["LobConfig", "config"]