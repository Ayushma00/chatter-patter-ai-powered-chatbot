from django.urls import path
from . import views

app_name = 'economics'
urlpatterns = [
    path('', views.economics_bot, name='economics'),
]
