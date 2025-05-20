from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import base, noticias_gnews
from .views import viaturas
from carros.api import api
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include('carros.urls')),
    path('', include('carros.urls')),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('api/noticias-artigos/', noticias_gnews, name='noticias_artigos'),
    path('servicos/', views.servicos, name='servicos'),
    path('viaturas/', viaturas, name='viaturas'),
    path("api/", api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







