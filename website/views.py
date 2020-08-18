from django.shortcuts import render
from django.http import HttpResponse
from .models import Case
# Create your views here.

def index(request):
    data = Case.objects.all()
    context = {
        'items': data,
    }
    return render(request, 'home.html', context)
