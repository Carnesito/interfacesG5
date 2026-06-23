from django.shortcuts import render

# Create your views here.
def listar_medicinas(request):
    return render(request, 'medicinas/listar_medicinas.html')