from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def games(request):
    return render(request, 'main/games.html')


def contact(request):
    return render(request, 'main/contact.html')


def topgames(request):
    return render(request, 'main/topgames.html')


def home(request):
    return render(request, 'main/home.html')
