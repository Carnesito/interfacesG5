from django.urls import path
from . import views

urlpatterns = [
    path('listar_resultados/', views.listar_resultados, name='listar_resultados'),
    path('crear_resultado/', views.crear_resultado, name='crear_resultado'),
    path('editar_resultado/<int:id>/', views.editar_resultado, name='editar_resultado'),
    path('eliminar_resultado/<int:id>/', views.eliminar_resultado, name='eliminar_resultado'),
]
