from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('hello', views.hello, name='hello'),
    path('play', views.play, name='play'),
    path('option', views.option, name='option'),
    path('check', views.check, name='check')
]