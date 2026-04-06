from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryOut(CategoryCreate):
    id: int 
    class Config:
        orm_mode = True

class MenuItemCreate(BaseModel):
    name : str
    price : float
    category_id : int
    description: str

class MenuItemOut(MenuItemCreate):
    id = int 
    class Config:
        orm_mode :True

class OrderCreate(BaseModel):
    address : str
    total :float
    phone_number :str
    starus:str

class OrderOut(OrderCreate):
    id : int
    class Config:
        orm_mode: True

class OrderItemCreate(BaseModel):
    menu_item: int
    quantity:int
    total:float
    order_id: int 

class OrderItemOut(OrderItemCreate):
    id : int 
    class Config:
        orm_mode : True




    