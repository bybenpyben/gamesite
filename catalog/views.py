from django.shortcuts import render
from .models import Game
from django.views.generic import DetailView


def catalog(request):
    games = Game.objects.all()
    return render(request, 'catalog/gamecatalog.html', {'games': games})


class GameDetailView(DetailView):
    model = Game
    template_name = 'catalog/gamedetail.html'
    context_object_name = 'game'


def catalog_janr(request):
    return render(request, 'catalog/janr.html')