from pydantic import BaseModel, field_validator


class InputModel(BaseModel):
    request: str

    @field_validator("request")
    @classmethod
    def validate_non_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field cannot be empty.")
        return v