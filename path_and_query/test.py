menu_items = {
    1: {
        "name": "Masala Dosa",
        "description": "Crispy dosa served with sambar and chutney",
        "price": 120,
        "category": "South Indian"
    },
    2: {
        "name": "Paneer Tikka",
        "description": "Grilled paneer with vegetables and spices",
        "price": 180,
        "category": "Starter"
    },
    3: {
        "name": "Veg Biryani",
        "description": "Aromatic basmati rice cooked with vegetables and spices",
        "price": 160,
        "category": "Main Course"
    },
    4: {
        "name": "Butter Naan",
        "description": "Soft naan topped with butter",
        "price": 50,
        "category": "Bread"
    },
    5: {
        "name": "Dal Makhani",
        "description": "Creamy black lentils cooked with Indian spices",
        "price": 140,
        "category": "Main Course"
    },
    6: {
        "name": "Cold Coffee",
        "description": "Chilled creamy coffee",
        "price": 100,
        "category": "Beverage"
    }
}

from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/hello")
def hello(name:str, age=int):
    return f"Hello {name}, Good Morning!, your age is {age}"

@app.get("/menu/{id}")
def menu_id(id:int):
    if id in menu_items.keys():
        return menu_items[id]

    return f"product not found for id {id}"

@app.get("/item")
def item_name(name:str):
    for i in menu_items:
        if menu_items[i]["name"] == name:
            return menu_items[i]

    return f"No item found"