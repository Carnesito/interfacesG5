from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Medicina
# Create your views here.
def listar_medicinas(request):
    Medicinas = Medicina.objects.all().order_by('id')
    return render(request, 'medicinas/listar_medicinas.html', {'medicinas': Medicinas})

def crear_medicinas(request):
    if request.method == 'POST': 
        Medicina.objects.create(
            nombre_medicina=request.POST.get('nombreMedicina'),
            precio_medicina=request.POST.get('precioMedicina'),
            stock_medicina=request.POST.get('stockMedicina'),
            estado_medicina=request.POST.get('estadoMedicina')
        )

        return redirect('listar_medicinas')
    return render(request, 'medicinas/crear_medicinas.html')



def eliminar_medicinas(request, id):
    medicina = Medicina.objects.get(id=id)
    medicina.delete()
    messages.success(request, "Medicina eliminada")
    return redirect('listar_medicinas')



def editar_medicinas(request, id):
    medicina= Medicina.objects.get(id=id)
    if request.method == 'POST':
        medicina.nombre_medicina = request.POST.get('nombre_medicina') 
        medicina.precio_medicina = request.POST.get('precio_medicina') 
        medicina.stock_medicina = request.POST.get('stock_medicina')
        medicina.estado_medicina = request.POST.get('estado_medicina')    

        medicina.save()
        messages.success(request, "Medicina actualizada")
        return redirect('listar_medicinas')
    return render(request, 'medicinas/editar_medicinas.html', {'medicina': medicina})     

