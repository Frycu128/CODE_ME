from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 0


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def wellcome(name: str):
    return f'Hello {name}'


@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Product):
    return item
