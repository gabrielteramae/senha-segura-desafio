from pydantic import BaseModel


class PasswordRequest(BaseModel):
    password: str


class ValidationErrorResponse(BaseModel):
    errors: list[str]
