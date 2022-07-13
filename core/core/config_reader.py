from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    django_secret_key: SecretStr
    django_debug_options: bool
    django_allowed_hosts: str

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'
        env_nested_delimiter = '__'


config = Settings()
