from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_host: str
    app_port: str
    app_port_local: str
    postgres_user: str
    postgres_db: str
    postgres_password: str
    postgres_port: str
    postgres_port_local: str
    db_migration_url: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()