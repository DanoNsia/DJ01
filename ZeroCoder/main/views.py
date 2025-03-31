from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def test(request):
    return HttpResponse("<h1>Это тестовая страница</h1>")

def data(request):
    return HttpResponse("<h1>Это дата</h1>")


