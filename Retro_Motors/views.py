from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Servico
import requests



def base(request):
    return render(request, 'base.html')  

def veiculos(request):
    return render(request, 'viaturas.html')

def index(request):
    return Httpresponse(request, 'index.html')

def home(request):
    return render(request, 'home.html')

@login_required
def menu(request):
    return render(request, 'base.html')


@csrf_exempt
def noticias_gnews(request):
    api_key = '77dbb86b4d3e4b0f2f97a305730a8df3'
    url = f'https://gnews.io/api/v4/top-headlines?token=77dbb86b4d3e4b0f2f97a305730a8df3&lang=pt'

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        return JsonResponse(dados)
    except Exception as e:
        return JsonResponse({'erro': 'Erro ao buscar notícias', 'detalhe': str(e)}, status=500)

params = {
    "q": "carro OR automóvel OR clássicos OR 'mundo automóvel'",
    "lang": "pt",
    "country": "pt",
    "max": 10,
    "apikey": settings.GNEWS_API_KEY
}

    
def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})


