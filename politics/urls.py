from django.urls import path
from . import views

app_name = 'politics'
urlpatterns = [
    path('', views.politics_bot, name='politics'),
]
