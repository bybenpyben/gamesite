from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView


def articles_list(request):
    news_list = Articles.objects.order_by('-pub_date')
    return render(request, 'news/news_home.html', {'news_list': news_list})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
