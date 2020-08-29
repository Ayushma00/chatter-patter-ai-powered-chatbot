from django.urls import path
from . import views

app_name = 'agriculture'
urlpatterns = [
    path('', views.agriculture_bot, name='agriculture'),
]
