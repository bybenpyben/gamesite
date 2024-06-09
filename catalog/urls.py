from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('janr', views.catalog_janr, name='janr'),

]
