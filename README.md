# E-Commerce API

A minimal FastAPI service exposing product-listing endpoints only. This is a trimmed-down version of a larger e-commerce API, keeping just the two read-only product endpoints.

## Features

- List all products, with optional filtering by category and minimum price
- Get details of a single product by ID
- In-memory data store, pre-seeded with sample products for easy testing

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn ecommerce_api_stripped:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

Interactive API docs (Swagger UI) are available at `http://127.0.0.1:8000/docs`.

## Endpoints

### `GET /`
Root endpoint. Returns basic API info and a list of available endpoints.

### `GET /products`
Returns a list of all products.

**Query parameters (optional):**
| Parameter    | Type   | Description                              |
|--------------|--------|------------------------------------------|
| `category`   | string | Filter products by category (case-insensitive) |
| `min_price`  | float  | Filter products with price >= this value |

**Example:**
```bash
curl "http://127.0.0.1:8000/products?category=electronics&min_price=20"
```

**Example response:**
```json
[
  {
    "product_id": 1,
    "name": "Laptop",
    "description": "High performance laptop",
    "price": 999.99,
    "stock": 10,
    "category": "electronics"
  }
]
```

### `GET /products/{product_id}`
Returns details for a single product.

**Path parameter:**
| Parameter    | Type | Description        |
|--------------|------|---------------------|
| `product_id` | int  | ID of the product   |

**Example:**
```bash
curl "http://127.0.0.1:8000/products/1"
```

**Example response:**
```json
{
  "product_id": 1,
  "name": "Laptop",
  "description": "High performance laptop",
  "price": 999.99,
  "stock": 10,
  "category": "electronics"
}
```

**Errors:**
- `404 Not Found` — if no product exists with the given `product_id`.

## Sample Data

The app seeds the following products on startup:

| ID | Name               | Price   | Category    | Stock |
|----|---------------------|---------|-------------|-------|
| 1  | Laptop              | 999.99  | electronics | 10    |
| 2  | Mouse               | 19.99   | electronics | 50    |
| 3  | Book: FastAPI Guide | 29.99   | books       | 5     |

## Notes

This is a stripped-down version of a larger API. Cart, order, customer, review, search, and product create/update/delete endpoints have been removed.
