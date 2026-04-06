from sqlalchemy import Session 
import models

def create_category(db: Session, data):
     obj = models.Category(**data.dict())
     db.add(obj)
     db.commit()
     db.refresh(obj)
     return obj

def get_categories(db : Session):
     return db.query(models.Category).all()

def create_menu_item(db: Session, data):
     obj = models.MenuItem(**data.dict())
     db.add(obj)
     db.commit()
     db.refresh(obj)
     return obj

def get_menu_item(db : Session):
     return db.query(models.MenuItem).all()

def get_menu_item(db : Session , item_id: int):
     return db.query(models.MenuItem).filter(models.MenuItem.id == item_id).first()

def create_order_item(db : Session, data):
     obj = models.OrderItems(**data.dict())
     db.add(obj)
     db.commit()
     db.refresh(obj)
     return obj

def get_order_item(db : Session):
     return db.query(models.OrderItems).all()

def update_order_item(db: Session, item_id: int, data):
    item = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()
    for key, value in data.dict().items():
        setattr(item, key, value)
    db.commit()
    return item

def delete_order_item(db: Session, item_id: int):
    item = db.query(models.OrderItem).filter(models.OrderItem.id == item_id).first()
    db.delete(item)
    db.commit()
     


