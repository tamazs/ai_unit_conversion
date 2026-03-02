from pydantic import BaseModel, field_validator

class OutputModel(BaseModel):
    response: str

    @field_validator("response")
    @classmethod
    def validate_non_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Field cannot be empty.")
        return v