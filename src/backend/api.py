from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Customer, Product
from .schemas import CustomerResponse, ProductCreate, ProductResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CSR Naive Agent API", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@app.get("/products/", response_model=list[ProductResponse])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Product).offset(skip).limit(limit).all()


@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
