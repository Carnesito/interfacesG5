from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('crear_usuarios/', views.crear_usuarios, name='crear_usuarios'),
    path('eliminar_usuarios/<int:id>/', views.eliminar_usuarios, name='eliminar_usuarios'),
    path('editar_usuarios/<int:id>/', views.editar_usuarios, name='editar_usuarios'),
]

