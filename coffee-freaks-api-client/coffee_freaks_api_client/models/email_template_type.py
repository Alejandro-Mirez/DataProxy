from enum import Enum

class EmailTemplateType(str, Enum):
    ACCOUNT_ALREADY_EXISTS = "ACCOUNT_ALREADY_EXISTS"
    REGISTRATION_TOKEN = "REGISTRATION_TOKEN"
    RESET_PASSWORD_TOKEN = "RESET_PASSWORD_TOKEN"

    def __str__(self) -> str:
        return str(self.value)
