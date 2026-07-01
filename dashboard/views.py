from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from pacientes.models import Paciente
from citas.models import Cita
from especialidades.models import Especialidad
from medicinas.models import Medicina

def dashboard(request):
    total_pacientes = Paciente.objects.count()
    total_citas = Cita.objects.count()
    total_especialidades = Especialidad.objects.count()
    total_medicinas = Medicina.objects.count()
    usuarios_recientes = User.objects.all().order_by('-date_joined')[:5]

    contexto = {
        'total_pacientes': total_pacientes,
        'total_citas': total_citas,
        'total_especialidades': total_especialidades,
        'total_medicinas': total_medicinas,
        'usuarios_recientes': usuarios_recientes,
    }
    return render(request, 'dashboard/dashboard.html', contexto)

def listar_usuarios(request):
    usuarios = User.objects.all().order_by('id')
    contexto = {
        'usuarios': usuarios
    }
    return render (request, 'dashboard/listar_usuarios.html',contexto)# siempre se va a usar dashboard/

def crear_usuarios(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Crear el usuario
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return render(request, 'dashboard/crear_usuarios.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return render(request, 'dashboard/crear_usuarios.html')
        #crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password)
      
        messages.success(request, "Usuario creado con exito.")
        return redirect('listar_usuarios')
    return render(request, 'dashboard/crear_usuarios.html')

def eliminar_usuarios(request, id):
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request, "Usuario eliminado con éxito.")
        return redirect('listar_usuarios')
   
def editar_usuarios(request, id): #metodo editar
     usuario = User.objects.get(id=id)
     if request.method == 'POST':
        username = request.POST.get('username_edit')
        email = request.POST.get('email_edit')
        password = request.POST.get('password_edit')
        #verificar si existe el usuario
        if User.objects.filter(username=username).exclude (id=id).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return render(request, 'dashboard/editar_usuarios.html',{'usuario': usuario})
        #verificar si existe el correo
        if User.objects.filter(email=email).exclude (id=id).exists():
            messages.error(request, "El correo electrónico ya existe.")
            return render(request, 'dashboard/editar_usuarios.html',{'usuario': usuario})
        #actualizar datos
        usuario.username = username
        usuario.email = email
        usuario.set_password(password)
        if password:
            usuario.set_password(password)
        usuario.save()
        messages.success(request, "Usuario actualizado con éxito.")
        return redirect('listar_usuarios')
     contexto = {
        'usuario': usuario  
     }
     return render(request, 'dashboard/editar_usuarios.html', contexto)