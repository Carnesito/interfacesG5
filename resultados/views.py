from django.shortcuts import render, redirect
from django.contrib import messages
from citas.models import Cita
from medicinas.models import Medicina
from .models import Resultado, DetalleResultadoMedicina

def listar_resultados(request):
    resultados = Resultado.objects.all().order_by('id')
    return render(request, 'resultados/listar_resultados.html', {'resultados': resultados})

def crear_resultado(request):
    citas_disponibles = Cita.objects.filter(resultado__isnull=True).exclude(estado='Finalizada')
    medicinas = Medicina.objects.all()

    if request.method == 'POST':
        cita_id = request.POST.get('cita')
        diagnostico = request.POST.get('diagnostico')
        indicaciones = request.POST.get('indicaciones')

        cita = Cita.objects.get(id=cita_id)

        resultado = Resultado.objects.create(
            cita=cita,
            diagnostico=diagnostico,
            indicaciones=indicaciones
        )

        cita.estado = 'Finalizada'
        cita.save()

        medicinas_seleccionadas = request.POST.getlist('medicinas_seleccionadas')
        for med_id in medicinas_seleccionadas:
            cantidad = int(request.POST.get(f'cantidad_{med_id}', 0))
            dosis = request.POST.get(f'dosis_{med_id}', '')

            if cantidad > 0:
                medicina = Medicina.objects.get(id=med_id)
                if medicina.stock_medicina >= cantidad:
                    medicina.stock_medicina -= cantidad
                    medicina.save()

                    DetalleResultadoMedicina.objects.create(
                        resultado=resultado,
                        medicina=medicina,
                        cantidad=cantidad,
                        dosis=dosis
                    )
                else:
                    messages.warning(request, f"Stock insuficiente para {medicina.nombre_medicina}. No se descontó.")

        messages.success(request, "Resultado registrado y medicamentos asignados con éxito.")
        return redirect('listar_resultados')

    context = {
        'citas': citas_disponibles,
        'medicinas': medicinas
    }
    return render(request, 'resultados/crear_resultados.html', context)

def editar_resultado(request, id):
    resultado = Resultado.objects.get(id=id)
    if request.method == 'POST':
        detalles_viejos = resultado.detalles_medicamentos.all()
        for det in detalles_viejos:
            med = det.medicina
            med.stock_medicina += det.cantidad
            med.save()
        
        resultado.detalles_medicamentos.all().delete()

        resultado.diagnostico = request.POST.get('diagnostico')
        resultado.indicaciones = request.POST.get('indicaciones')
        resultado.save()

        medicinas_seleccionadas = request.POST.getlist('medicinas_seleccionadas')
        for med_id in medicinas_seleccionadas:
            cantidad = int(request.POST.get(f'cantidad_{med_id}', 0))
            dosis = request.POST.get(f'dosis_{med_id}', '')

            if cantidad > 0:
                medicina = Medicina.objects.get(id=med_id)
                if medicina.stock_medicina >= cantidad:
                    medicina.stock_medicina -= cantidad
                    medicina.save()

                    DetalleResultadoMedicina.objects.create(
                        resultado=resultado,
                        medicina=medicina,
                        cantidad=cantidad,
                        dosis=dosis
                    )
                else:
                    messages.warning(request, f"Stock insuficiente para {medicina.nombre_medicina}. No se descontó.")

        messages.success(request, "Resultado y receta médica actualizados con éxito.")
        return redirect('listar_resultados')

    medicinas = Medicina.objects.all().order_by('id')
    medicinas_list = []
    for med in medicinas:
        detalle = DetalleResultadoMedicina.objects.filter(resultado=resultado, medicina=med).first()
        medicinas_list.append({
            'medicina': med,
            'asignada': detalle is not None,
            'cantidad': detalle.cantidad if detalle else 0,
            'dosis': detalle.dosis if detalle else ''
        })

    return render(request, 'resultados/editar_resultados.html', {
        'resultado': resultado,
        'medicinas_list': medicinas_list
    })

def eliminar_resultado(request, id):
    resultado = Resultado.objects.get(id=id)
    detalles = resultado.detalles_medicamentos.all()
    for detalle in detalles:
        medicina = detalle.medicina
        medicina.stock_medicina += detalle.cantidad
        medicina.save()

    cita = resultado.cita
    cita.estado = 'Pendiente'
    cita.save()

    resultado.delete()
    messages.success(request, "Resultado eliminado y stock de medicamentos restablecido.")
    return redirect('listar_resultados')
