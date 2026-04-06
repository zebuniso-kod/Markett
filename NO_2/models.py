from sqlalchemy import Column , Integer, String , ForeignKey , Float
from database import Base 

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True, index = True)
    name = Column (String)

class MenuItem(Base) :
    __tablename__ = "Menu_item"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(String)

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key = True, index = True)
    address = Column(String)
    total = Column(Float)
    phone_number = Column(Float)
    Status = Column(String)

class OrderItems(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key = True, index = True)
    menu_item = Column(Integer, ForeignKey = ("manu_item.id"))
    quantity = Column(Integer)
    total = Column(Float)
    order_id = Column(Integer, ForeignKey ("order.id"))
