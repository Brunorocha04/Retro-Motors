# schemas.py
from ninja import Schema

class CarroSchema(Schema):
    id: int
    marca: str
    modelo: str
    ano: int
    preco: float
    imagem: str  # URL
