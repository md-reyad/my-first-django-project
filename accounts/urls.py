from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

from . import views
urlpatterns = [

    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),

    path('logout/', auth_views.logout),
    path('index', views.index),
    path('notice-list', views.notice_list, name='notice_list'),
    path('create-notice', views.create_notice),
    path('notice-save', views.create_notice),
    # path('logout', views.logout),

]