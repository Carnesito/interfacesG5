from django.urls import path
from . import views

urlpatterns = [
    path('listar_citas/', views.listar_citas, name='listar_citas'),
    path('crear_cita/', views.crear_cita, name='crear_cita'),
    path('editar_cita/<int:id>/', views.editar_cita, name='editar_cita'),
    path('eliminar_cita/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
]
