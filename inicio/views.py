from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'index.html')

def doctores(request):
    return render(request, 'doctors.html')

def departamentos(request):
    return render(request, 'departments.html')

def citas(request):
    return render(request, 'citas.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            mensaje = 'Usuario o contraseña incorrectos'
    return render(request, 'login.html', {'mensaje': mensaje})