# from datetime import datetime
# from typing import List, Optional
#
# from pydantic import BaseModel, Field
# from pydantic.types import UUID4, condecimal
#
#
# def to_camel(string: str) -> str:
#     if "_" not in string:
#         return string
#     words = string.split("_")
#     words = [words[0]] + [word.capitalize() for word in words[1:]]
#     return "".join(words)
#
#
# class ProductBase(BaseModel):
#     class Config:
#         alias_generator = to_camel
#         allow_population_by_field_name = True
#
#
# class ProductUpdate(ProductBase):
#     name: Optional[str]
#     price: Optional[condecimal(decimal_places=2)]  # type: ignore
#
#
# class ProductCreate(ProductBase):
#     store_id: UUID4
#     name: str
#     price: condecimal(decimal_places=2)  # type: ignore
#
#
# class Product(ProductCreate):
#     product_id: UUID4
#
#     class Config:
#         orm_mode = True
#
#
# class OrderItemCreate(BaseModel):
#     product_id: UUID4
#     quantity: int = Field(..., gt=0)
#
#     class Config:
#         orm_mode = True
#         alias_generator = to_camel
#         allow_population_by_field_name = True
#
#
# class OrderCreate(BaseModel):
#     items: List[OrderItemCreate]
#
#
# class Order(BaseModel):
#     order_id: UUID4
#     date: datetime
#
#     class Config:
#         orm_mode = True
#         alias_generator = to_camel
#         allow_population_by_field_name = True
#
#
# class OrderItem(BaseModel):
#     quantity: int = Field(..., gt=0)
#     product: Product
#
#     class Config:
#         orm_mode = True
#         alias_generator = to_camel
#         allow_population_by_field_name = True
#
#
# class OrderDetail(Order):
#     order_id: UUID4
#     date: datetime
#     items: List[OrderItem]
