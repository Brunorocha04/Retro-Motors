# api.py

# carros/api.py
from ninja import NinjaAPI
from .models import Carro
from .schemas import CarroSchema

api = NinjaAPI()

@api.get("/carros", response=list[CarroSchema])
def listar_carros(request):
    carros = Carro.objects.all()
    return [
        CarroSchema(
            id=carro.id,
            marca=carro.marca,
            modelo=carro.modelo,
            ano=carro.ano,
            preco=carro.preco,
            imagem=request.build_absolute_uri(carro.imagem.url) if carro.imagem else "",
            descricao=carro.descricao,
            km=carro.km,
            combustivel=carro.combustivel
        )
        for carro in carros
    ]
