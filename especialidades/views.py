from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Especialidad

def listar_especialidades(request):
    especialidades = Especialidad.objects.all().order_by('id')
    return render(request, 'especialidades/listar_especialidades.html', {'especialidades': especialidades})

def crear_especialidad(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        costo = request.POST.get('costo')

        Especialidad.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            costo=costo
        )
        messages.success(request, "Especialidad creada con éxito.")
        return redirect('listar_especialidades')
    return render(request, 'especialidades/crear_especialidades.html')

def editar_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    if request.method == 'POST':
        especialidad.nombre = request.POST.get('nombre')
        especialidad.descripcion = request.POST.get('descripcion')
        especialidad.costo = request.POST.get('costo')
        especialidad.save()
        messages.success(request, "Especialidad actualizada con éxito.")
        return redirect('listar_especialidades')
    return render(request, 'especialidades/editar_especialidades.html', {'especialidad': especialidad})

def eliminar_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    especialidad.delete()
    messages.success(request, "Especialidad eliminada.")
    return redirect('listar_especialidades')
