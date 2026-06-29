from django.urls import path
from . import views 
urlpatterns = [
    path('listar_medicina', views.listar_medicinas, name='listar_medicinas'),
    path('crear_medicina', views.crear_medicinas, name='crear_medicinas'),
    path('eliminar_medicina/<int:id>/', views.eliminar_medicinas, name='eliminar_medicinas'),
    path('editar_medicina/<int:id>/', views.editar_medicinas, name='editar_medicinas'),
]       