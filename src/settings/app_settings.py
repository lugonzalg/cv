from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings
from pydantic import computed_field

import warnings
from typing_extensions import Self


class AppSettings(BaseSettings):
    # Database settings
    DB_SCHEME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # ENVIRONMENT: str

    @computed_field
    @property
    def DB_URL(self) -> MultiHostUrl:
        return MultiHostUrl.build(
            scheme=self.DB_SCHEME,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value == "changethis":
            message = (
                f'The value of {var_name} is "changethis", '
                "for security, please change it, at least for deployments."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)

    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("POSTGRES_PASSWORD", self.DB_PASSWORD)

        return self
