from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Servico
from datetime import datetime
import random
from datetime import date
from .models import Carro
import requests



def base(request):
    return render(request, 'base.html')  

def home(request):
    return render(request, 'home.html')

@login_required
def menu(request):
    return render(request, 'base.html')


@csrf_exempt
def noticias_gnews(request):
    api_key = '29cc91ade1e267a4804602ecdfef364c'
    url = f'https://gnews.io/api/v4/search?q=carros+clássicos&token={api_key}&lang=pt'

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        noticias = dados.get('articles', [])  # <- extrai a lista de artigos

        return render(request, 'noticias_artigos.html', {'noticias': noticias})
    
    except Exception as e:
        return render(request, 'noticias_artigos.html', {
            'noticias': [],
            'erro': f'Erro ao buscar notícias: {str(e)}'
        })

    
def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

def viaturas(request):
    url = "https://api-ninjas.com/profile"
    headers = {
        "X-Api-Key": "/J4nUagNBnBu/9hj+RyKEQ==FrK66CJXXddHnS7q"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        api_data = response.json()
    else:
        api_data = []

    # Mapeia os dados no formato esperado pelo template
    veiculos = []
    for car in api_data:
        veiculos.append({
            'marca': car.get('make', 'Desconhecida'),
            'modelo': car.get('model', 'Desconhecido'),
            'ano': car.get('year', 'N/A'),
            'combustivel': car.get('fuel_type', 'N/A'),
            'km': 'N/A',  # A API do Ninja Cars não tem km
            'descricao': f"{car.get('make')} {car.get('model')} ({car.get('class')})",
            'imagem': 'https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg'  # Imagem genérica
        })

    # Marcas disponíveis e marcas ativas dos filtros
    marcas_disponiveis = list(set([v['marca'] for v in veiculos]))
    marcas_ativas = request.GET.getlist("marcas")

    # Filtro por marcas
    if marcas_ativas:
        veiculos = [v for v in veiculos if v['marca'] in marcas_ativas]
        
    return render(request, 'viaturas.html', {
        'veiculos': veiculos,
        'marcas_disponiveis': marcas_disponiveis,
        'marcas_ativas': marcas_ativas
    })

def index(request):
    random.seed(date.today().toordinal())  # semente diária

    viaturas = list(Carro.objects.all())
    destaques = random.sample(viaturas, min(3, len(viaturas)))  # escolhe até 3

    return render(request, 'index.html', {'destaques': destaques})