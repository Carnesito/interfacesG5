from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
from django.contrib.auth.decorators import login_required
>>>>>>> respaldo-local

def inicio(request):
    return render(request, 'index.html')

def doctores(request):
    return render(request, 'doctors.html')

def departamentos(request):
    return render(request, 'departments.html')

def citas(request):
    return render(request, 'citas.html')

<<<<<<< HEAD
=======
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

>>>>>>> respaldo-local
def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        user_exists = User.objects.filter(username=username).exists()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            if user_exists:
                mensaje = 'La contraseña es incorrecta. Por favor, inténtelo de nuevo.'
            else:
                mensaje = 'El usuario ingresado no existe.'
    return render(request, 'login.html', {'mensaje': mensaje})
