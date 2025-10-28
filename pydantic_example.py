from  pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")

user_data = {
    "id": 123,
    "name": "Max",
    "email": "max@mail.ru",
    "isActive": True
}

user = User(**user_data)

class Short(BaseModel):
    id: int
    email: str

class Loong(Short):
    name: str
    age: int

