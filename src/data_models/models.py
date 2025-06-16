from pydantic import BaseModel


class ItemResponse(BaseModel):
    title: str
    description: str



