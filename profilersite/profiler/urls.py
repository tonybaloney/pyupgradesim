from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('tasks', views.tasks, name='tasks'),
    path('results', views.results, name='results'),
    path('reset', views.reset, name='reset'),
]