# 定义learning_logs的URL模式

# from django.conf.urls import url
from django.urls import path

# from learning_logs.views import index as myindex
# from learning_logs import views as myview
# from learning_logs import views
# 页面穿不进learning_log\urls.py
from . import views

app_name = 'learning_logs'

urlpatterns = [
    #     主页
    #    Django在urlpatterns 中查找与请求的URL字符串匹配的正则表达式
    path('', views.index, name="index"),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
