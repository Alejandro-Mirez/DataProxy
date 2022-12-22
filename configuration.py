from pydantic import BaseSettings

class Settings(BaseSettings):
    api_host: str = "http://192.168.68.101:9999"
    api_user: str = "admin"
    api_password: str = "admin"


settings = Settings()
