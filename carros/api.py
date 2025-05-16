# api.py
from ninja import NinjaAPI
from .models import Carro
from .schemas import CarroSchema
from django.conf import settings

api = NinjaAPI()

@api.get("/carros-destaque", response=list[CarroSchema])
def carros_destaque(request):
    carros = Carro.objects.all()[:6]  # ou .filter(destaque=True)
    return [
        CarroSchema(
            id=carro.id,
            marca=carro.marca,
            modelo=carro.modelo,
            ano=carro.ano,
            preco=carro.preco,
            imagem=request.build_absolute_uri(carro.imagem.url) if carro.imagem else ""
        )
        for carro in carros
    ]

    from ninja import NinjaAPI

api = NinjaAPI()

