from django.urls import path
from . import views

urlpatterns = [
    path('listar_pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('editar_paciente/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar_paciente/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
]
