from django.urls import path
from . import views
 # Importa as views do próprio app

urlpatterns = [
    path('viaturas/', views.viaturas_views, name='viaturas'),
]
