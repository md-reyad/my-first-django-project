from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "html/index.html")


def hi(request):
    return render(request, "html/index.html")


def acadamicHistory(request):
    return render(request, "html/acadamic_history.html")