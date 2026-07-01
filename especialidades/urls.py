from django.urls import path
from . import views

urlpatterns = [
    path('listar_especialidades/', views.listar_especialidades, name='listar_especialidades'),
    path('crear_especialidad/', views.crear_especialidad, name='crear_especialidad'),
    path('editar_especialidad/<int:id>/', views.editar_especialidad, name='editar_especialidad'),
    path('eliminar_especialidad/<int:id>/', views.eliminar_especialidad, name='eliminar_especialidad'),
]
