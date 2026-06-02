from django.contrib import admin
from django.urls import path   , include                                     
from . import views
urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('doctores/',views.doctores, name='doctores'),
    path('departamentos/',views.departamentos, name='departamentos'),
    path('citas/',views.citas, name='citas'),
    path('login/',views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')

]
