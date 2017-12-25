from django.urls import path

from . import views

urlpatterns = [
    path('form', views.index, name='index'),
    path('reyad', views.reyad, name='reyad'),
    path('list', views.list, name='list'),
    # path('saveItem', views.saveItem, name='saveItem'),
]