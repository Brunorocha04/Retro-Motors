# carros/schemas.py
from pydantic import BaseModel

class CarroSchema(BaseModel):
    id: int
    marca: str
    modelo: str
    ano: int
    preco: float
    imagem: str
    descricao: str
    km: int
    combustivel: str

