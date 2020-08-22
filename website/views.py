from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from json import dumps
from .models import Case
from datetime import datetime
# Create your views here.
baseUrl = "https://api.covidtracking.com/v1/states/ny/daily.json"
response = requests.get(baseUrl)
content = response.content
data = json.loads(content)

#just to convert the visualization of the date
for datum in data:
    oldFormat = str(datum['date'])
    datetimeobject = datetime.strptime(oldFormat, '%Y%m%d')
    newFormat = datetimeobject.strftime('%m-%d-%Y')
    datum['date'] = newFormat

    noneType = str(datum['recovered'])
    if(noneType == "None"):
        datum['recovered'] = 0

    noneTypeD = str(datum['death'])
    if(noneTypeD == "None"):
        datum['death'] = 0

    noneTypeH = str(datum['hospitalizedCurrently'])
    if(noneTypeH == "None"):
        datum['hospitalizedCurrently'] = 0
        


def index(request):
    #Gets minimum and max increase in cases
    maxIncrease = max(data, key=lambda ev: ev['positiveIncrease'])
    minIncrease = min(data, key=lambda ev: ev['positiveIncrease'])

    #Gets minimum and max increase in deaths
    maxDeath = max(data, key=lambda ev: ev['deathIncrease'])
    minDeath = min(data, key=lambda ev: ev['deathIncrease'])
 

    context = {
        'maxD': maxDeath,
        'minD': minDeath,
        'minI': minIncrease,
        'maxI': maxIncrease,
        'cases': data,
    }
    return render(request, 'home.html', context)

def adv_metrics(request):
    #Getting the added recoveries per day
    for i in range(0, len(data) - 1):
        x = data[i]["recovered"] - data[i + 1]["recovered"]
        y = data[i]["hospitalizedCurrently"] - data[i + 1]["hospitalizedCurrently"]
        data[i].update(recoveryIncrease = x)
        data[i].update(hospInc = y)
        

    #Separating the cases into a list
    listCases = []
    for case in data:
        listCases.append(case['positive'])

    context = {
        'cases': data,
        'listPositive': listCases,
    }
    return render(request, 'advance_metrics.html', context)

def compare_by_state(request):
     return render(request, 'advance_metrics.html')