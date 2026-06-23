from django.urls import path
from . import views 
urlpatterns = [
    path('', views.listar_medicinas, name='listar_medicinas'),
]       