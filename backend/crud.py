from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import ProductModel


# get all products
def get_products(db: Session, product_id: int):
    """ 
    função que retorna totos os produto pelo id
    """
    return db.query(ProductModel).all()


# get where id = id
def get_product(db: Session, product_id: int):
    """
    Função que retorna um produto pelo id
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first

# insert into
def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# delete where id = id
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


# update where id = id
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.categoria is not None:
        db_product.categoria = product.categoria

    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    db.refresh(db_product)
    return db_product