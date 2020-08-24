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
    newFormat = datetimeobject.strftime('%m/%d/%Y')
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
    extremeNumbers = []
    extremeNumbers.append(max(data, key=lambda ev: ev['positiveIncrease']))
    extremeNumbers.append(min(data, key=lambda ev: ev['positiveIncrease']))
    extremeNumbers.append(max(data, key=lambda ev: ev['deathIncrease']))
    extremeNumbers.append(min(data, key=lambda ev: ev['deathIncrease']))
    
    listCases = []
    listDate = []
    listDeath = []
    listHosp = []
    listRec = []
    for case in data:
        listCases.append(case['positiveIncrease'])
        listDate.append(case['date'])
        listDeath.append(case['deathIncrease'])
        listHosp.append(case['hospitalizedCurrently'])
        listRec.append(case['recovered'])

    listCases = json.dumps(listCases)
    listDate = json.dumps(listDate)
    listDeath = json.dumps(listDeath)
    listHosp = json.dumps(listHosp)
    listRec = json.dumps(listRec)

    for i in range(0, len(data) - 1):
        x = data[i]["recovered"] - data[i + 1]["recovered"]
        data[i].update(recoveryIncrease = x)

    context = {
        'extremeNumbers': extremeNumbers,
        'cases': data,
        'listPositive': listCases,
        'listDates': listDate,
        'listDeaths': listDeath,
        'listHosp': listHosp,
        'listRec': listRec
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
    context = {
        'cases': data, 
    }
    return render(request, 'advance_metrics.html', context)

def compare_by_state(request):
    text = ""
    comparedData = []
    diff = []
    if request.method == "POST":
        text = request.POST.get('dropdown', '')
        comparedLink = "https://api.covidtracking.com/v1/states/" + text + "/daily.json"
        comparedResp = requests.get(comparedLink)
        comparedCont = comparedResp.content
        comparedData = json.loads(comparedCont)

        for datum in comparedData:
            oldFormat = str(datum['date'])
            datetimeobject = datetime.strptime(oldFormat, '%Y%m%d')
            newFormat = datetimeobject.strftime('%m/%d/%Y')
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
        diff.append(abs(data[0]["positive"] - comparedData[0]["positive"]))

    context = {
        'comparedData': comparedData,
        'cases': data,
        'differences': diff,
    }
    return render(request, 'compare_by_state.html', context)