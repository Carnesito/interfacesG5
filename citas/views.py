from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from pacientes.models import Paciente
from especialidades.models import Especialidad
from .models import Cita

def listar_citas(request):
    citas = Cita.objects.all().order_by('id')
    return render(request, 'citas/listar_citas.html', {'citas': citas})

def crear_cita(request):
    pacientes = Paciente.objects.all()
    doctores = User.objects.all()
    especialidades = Especialidad.objects.all()

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        doctor_id = request.POST.get('doctor')
        especialidad_id = request.POST.get('especialidad')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        motivo = request.POST.get('motivo_consulta')

        paciente = Paciente.objects.get(id=paciente_id)
        doctor = User.objects.get(id=doctor_id)
        especialidad = Especialidad.objects.get(id=especialidad_id)

        Cita.objects.create(
            paciente=paciente,
            doctor=doctor,
            especialidad=especialidad,
            fecha=fecha,
            hora=hora,
            motivo_consulta=motivo
        )
        messages.success(request, "Cita agendada con éxito.")
        return redirect('listar_citas')

    context = {
        'pacientes': pacientes,
        'doctores': doctores,
        'especialidades': especialidades
    }
    return render(request, 'citas/crear_citas.html', context)

def editar_cita(request, id):
    cita = Cita.objects.get(id=id)
    pacientes = Paciente.objects.all()
    doctores = User.objects.all()
    especialidades = Especialidad.objects.all()

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        doctor_id = request.POST.get('doctor')
        especialidad_id = request.POST.get('especialidad')
        cita.fecha = request.POST.get('fecha')
        cita.hora = request.POST.get('hora')
        cita.motivo_consulta = request.POST.get('motivo_consulta')
        cita.estado = request.POST.get('estado')

        cita.paciente = Paciente.objects.get(id=paciente_id)
        cita.doctor = User.objects.get(id=doctor_id)
        cita.especialidad = Especialidad.objects.get(id=especialidad_id)
        cita.save()

        messages.success(request, "Cita actualizada con éxito.")
        return redirect('listar_citas')

    context = {
        'cita': cita,
        'pacientes': pacientes,
        'doctores': doctores,
        'especialidades': especialidades
    }
    return render(request, 'citas/editar_citas.html', context)

def eliminar_cita(request, id):
    cita = Cita.objects.get(id=id)
    cita.delete()
    messages.success(request, "Cita eliminada.")
    return redirect('listar_citas')
