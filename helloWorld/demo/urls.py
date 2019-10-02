'''
Created on 25 sep. 2019

@author: TIJUANA
'''
from django.urls import path

from . import views
from . import codigo

pp_name = 'demo'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('registro/', codigo.registro, name='registro'),
    path('mensaje/', views.mensaje, name='mensaje'),

    # ex: /polls/5/
    path('test/', views.detail, name='test'),


]