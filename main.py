"""
E-COMMERCE API
----------------------------------
Only 2 endpoints:
  1. GET /products         -> list all products
  2. GET /products/{id}    -> get a single product

"""



from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(title="Dummy E-Commerce API", version="1.0")

# ---------- In-memory "database" ----------
products_db = {}

# ---------- Helper functions ----------
def get_product_or_404(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

# ========== PRODUCTS ==========

# 1. List all products
@app.get("/products")
async def list_products(category: Optional[str] = None, min_price: Optional[float] = None):
    result = list(products_db.values())
    if category:
        result = [p for p in result if p["category"].lower() == category.lower()]
    if min_price:
        result = [p for p in result if p["price"] >= min_price]
    return result

# 2. Get single product
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return get_product_or_404(product_id)

# ========== ROOT endpoint ==========
@app.get("/")
async def root():
    return {
        "api": "E-Commerce API (Stripped)",
        "version": "1.0",
        "endpoints": [
            "GET /products",
            "GET /products/{id}"
        ]
    }

# Seed some demo data for easier testing
@app.on_event("startup")
def seed_data():
    if not products_db:
        products_db[1] = {
            "product_id": 1,
            "name": "Laptop",
            "description": "High performance laptop",
            "price": 999.99,
            "stock": 10,
            "category": "electronics"
        }
        products_db[2] = {
            "product_id": 2,
            "name": "Mouse",
            "description": "Wireless mouse",
            "price": 19.99,
            "stock": 50,
            "category": "electronics"
        }
        products_db[3] = {
            "product_id": 3,
            "name": "Book: FastAPI Guide",
            "description": "Learn FastAPI",
            "price": 29.99,
            "stock": 5,
            "category": "books"
        }
