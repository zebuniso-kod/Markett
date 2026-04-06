from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal , engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.post("/catigories/")
def create_category(data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, data)

@app.get("/catigories/")
def create_categoty(db : Session = Depends(get_db)):
    return crud.create_categories(db)

@app.post("/menu-items/")
def create_menu_item(data: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return crud.create_menu_item(db, data)

@app.get("/menu-items/")
def get_menu_items(db: Session = Depends(get_db)):
    return crud.get_menu_items(db)

@app.get("/menu-items/{id}")
def get_menu_item(id: int, db: Session = Depends(get_db)):
    return crud.get_menu_item(db, id)

@app.post("/orders/")
def create_order(data: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, data)

@app.get("/orders/")
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.get("/orders/{id}")
def get_order(id: int, db: Session = Depends(get_db)):
    return crud.get_order(db, id)

@app.post("/order-items/")
def create_order_item(data: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_item(db, data)

@app.get("/order-items/")
def get_order_items(db: Session = Depends(get_db)):
    return crud.get_order_items(db)

@app.put("/order-items/{id}")
def update_order_item(id: int, data: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.update_order_item(db, id, data)

@app.delete("/order-items/{id}")
def delete_order_item(id: int, db: Session = Depends(get_db)):
    return crud.delete_order_item(db, id)




