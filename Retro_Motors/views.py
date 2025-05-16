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


def carros_api_view(request):
    modelo = request.GET.get('q', 'camry')  # busca pelo modelo inserido na barra de pesquisa
    marcas_ativas = request.GET.getlist('marcas')
    # Chave da API e endpoint
    api_key = '/J4nUagNBnBu/9hj+RyKEQ==FrK66CJXXddHnS7q'  # <- substitui pela tua chave da API
    url = f'https://api.api-ninjas.com/v1/cars?model={modelo}'

    headers = {
        'X-Api-Key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados = response.json()
        print("RESULTADO API:", dados)
        print("RESPOSTA BRUTA:", response.text)

        # Aplicar filtro por marcas, se houver
        if marcas_ativas:
            dados = [carro for carro in dados if carro['make'] in marcas_ativas]

        # Lista única de marcas para os filtros
        marcas_disponiveis = sorted(set(carro['make'] for carro in dados))

        # Simular campos extra para o template (imagens, descrição, km, etc.)
        for carro in dados:
            carro['marca'] = carro['make']
            carro['modelo'] = carro['model']
            carro['descricao'] = carro.get('class', 'Sem descrição')
            carro['ano'] = carro.get('year', 'N/A')
            carro['km'] = 100000  # valor fictício
            carro['combustivel'] = carro.get('fuel_type', 'Gasolina')
            carro['imagem'] = f"https://via.placeholder.com/150?text={carro['make']}+{carro['model']}"

    else:
        dados = []
        marcas_disponiveis = []

    context = {
    'veiculos': dados,
    'marcas_disponiveis': marcas_disponiveis,
    'marcas_ativas': marcas_ativas,
}
    return render(request, 'viaturas.html', context)

def index(request):
    random.seed(date.today().toordinal())  # semente diária

    viaturas = list(Carro.objects.all())
    destaques = random.sample(viaturas, min(3, len(viaturas)))  # escolhe até 3

    return render(request, 'index.html', {'destaques': destaques})