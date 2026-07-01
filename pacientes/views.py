from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Paciente

def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by('id')
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')

        if Paciente.objects.filter(cedula=cedula).exists():
            messages.error(request, "Ya existe un paciente con esta cédula.")
            return render(request, 'pacientes/crear_pacientes.html')

        Paciente.objects.create(
            nombre_completo=nombre_completo,
            cedula=cedula,
            telefono=telefono,
            correo=correo
        )
        messages.success(request, "Paciente registrado con éxito.")
        return redirect('listar_pacientes')
    return render(request, 'pacientes/crear_pacientes.html')

def editar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'POST':
        paciente.nombre_completo = request.POST.get('nombre_completo')
        paciente.cedula = request.POST.get('cedula')
        paciente.telefono = request.POST.get('telefono')
        paciente.correo = request.POST.get('correo')
        paciente.save()
        messages.success(request, "Paciente actualizado con éxito.")
        return redirect('listar_pacientes')
    return render(request, 'pacientes/editar_pacientes.html', {'paciente': paciente})

def eliminar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    messages.success(request, "Paciente eliminado.")
    return redirect('listar_pacientes')
