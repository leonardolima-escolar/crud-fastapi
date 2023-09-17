from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = dict()


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: str | None = None


@app.get("/products")
def list_products():
    return products


@app.post("/products")
def create_product(product: Product):
    if not products.get(product.id):
        products[product.id] = product
        return product
    raise HTTPException(status_code=400, detail="Product already exists.")


@app.get("/products/{product_id}")
def read_product(product_id: int):
    product = products.get(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    product = products.get(product_id)
    if product:
        products[product.id] = updated_product
        return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    product = products.get(product_id)
    if product:
        return products.pop(product_id)
    raise HTTPException(status_code=404, detail="Product not found")
