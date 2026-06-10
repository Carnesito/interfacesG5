from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse

# Create your views here.
=======
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
>>>>>>> respaldo-local
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
