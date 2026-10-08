from pydantic import BaseModel 

class MenuItem(BaseModel):
    name: str
    description: str
    price: float
    category: str


class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    data: list[MenuItem]