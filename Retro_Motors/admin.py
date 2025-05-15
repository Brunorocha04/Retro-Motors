from django.contrib import admin
from .models import Carro
from .models import Servico

admin.site.register(Carro)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'destaque')
    list_filter = ('categoria', 'destaque')
    search_fields = ('titulo', 'descricao')
