from pydantic.v1 import BaseSettings

class ServerSettings(BaseSettings):
    DATABASE_URL : str
    class Config:
        env_file = ".env"

server_settings = ServerSettings()