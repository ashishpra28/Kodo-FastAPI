from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
# from fastapi.responses import HTMLResponse

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

