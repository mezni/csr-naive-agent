from pydantic import BaseModel


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    tier: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    price: float
    category: str


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
