from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include('carros.urls')),  
    path('', menu, name='menu'),
    path('accounts/', include('accounts.urls')),
    path('', include('carros.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





