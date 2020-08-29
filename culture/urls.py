from django.urls import path
from . import views

app_name = 'culture'
urlpatterns = [
    path('', views.culture_bot, name='culture'),
]
