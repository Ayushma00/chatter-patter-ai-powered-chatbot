from django.shortcuts import render
import requests


def home(request):
    res = requests.get("https://nepalcorona.info/api/v1/data/nepal")
    data = res.json()
    return render(request, 'home/index.html', {"positive": data["tested_positive"], "recovered": data["recovered"], "deaths": data["deaths"]})
