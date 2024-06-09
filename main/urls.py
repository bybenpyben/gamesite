from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('games', views.games, name='games'),
    path('contact', views.contact, name='contact'),
    path('topgames', views.topgames, name='topgames'),
]
