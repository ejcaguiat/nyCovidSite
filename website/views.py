from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Case
# Create your views here.
baseUrl = "https://api.covidtracking.com/v1/states/va/daily.json"
response = requests.get(baseUrl)
content = response.content
data = json.loads(content)

def index(request):
    context = {
        'cases': data,
    }
    return render(request, 'home.html', context)

def adv_metrics(request):
    context = {
        'cases': data,
    }
    return render(request, 'advance_metrics.html', context)

def compare_by_state(request):
     return render(request, 'advanced_metrics.html')