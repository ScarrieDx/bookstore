from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Wenas tardes esta es la Home page</h1>")

