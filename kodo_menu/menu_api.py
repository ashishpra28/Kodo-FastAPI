from fastapi import FastAPI 

app = FastAPI(
    title="Kodo Menu API",
    description="API for managing Kodo Menu items and categories.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to the Kodo Menu API!"}

