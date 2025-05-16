from django.contrib import admin
from .models import Carro
from .models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque')
    list_filter = ('categoria', 'destaque')
    search_fields = ('titulo', 'descricao')

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'ano', 'preco']
