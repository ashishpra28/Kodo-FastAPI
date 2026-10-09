from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse 
from data import menu_items
from models import MenuResponse, MenuItem

app = FastAPI(
    title="Kodo Menu API",
    description="API for managing Kodo Menu items and categories.",
    version="1.0.0"
)

# @app.get("/", response_class=HTMLResponse)
# def home():
#     return f"<h1>Welcome to Kodo Menu API</h1><p>Use the endpoints to manage menu items and categories.</p>"

@app.get("/")
def home():
    return {"message": "Welcome to Kodo Menu API. Use the endpoints to manage menu items and categories."}

@app.get("/menu", response_model=MenuResponse)
def get_menu(category: str | None = Query(default=None)):
    items = list(menu_items.values())

    if category:
        items = [
            item for item in items
            if item["category"].lower() == category.lower()
        ]

        if not items:
            raise HTTPException(status_code=404, detail="No item found")

    return MenuResponse(count=len(items), data=items)

@app.get("/menu/{item_id}", response_model=MenuResponse)
def menu_id(item_id:int):
    if item_id in menu_items:
        item = menu_items[item_id]
        return MenuResponse(count=1, data=[item])
    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )