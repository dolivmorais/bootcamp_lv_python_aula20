from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductCreate, ProductUpdate, ProductRead
from typing import List
from crud import create_product, get_products, get_product, delete_product, update_product


router = APIRouter()

@router.get("/products/", response_model=List[ProductRead], status_code=status.HTTP_200_OK)
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

@router.get("/products/{product_id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product

@router.post("/products/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.put("/products/{product_id}", response_model=ProductRead, status_code=status.HTTP_200_OK)    
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return update_product(db=db, product_id=product_id, product=product)

@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    delete_product(db=db, product_id=product_id)


