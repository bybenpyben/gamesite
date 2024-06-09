from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),

]
