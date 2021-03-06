from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

# Create your views here.
from .models import Topic


def index(request):
    # 学习笔记的主页
    # template = loader.get_template(learning_logs/index.html)
    return render(request, 'learning_logs/index.html')


def topics(request):
    # 显示所有主题
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
