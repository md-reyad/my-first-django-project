from django.urls import path

from . import views

urlpatterns = [
    path('form', views.index, name='index'),
    path('reyad', views.reyad, name='reyad'),
    path('list', views.list, name='list'),
    path('edit/<id>', views.edit),
    path('update/<id>', views.update),

    # path('saveItem', views.saveItem, name='saveItem'),
]