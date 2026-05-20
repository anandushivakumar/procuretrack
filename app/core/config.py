from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    secret_key: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()