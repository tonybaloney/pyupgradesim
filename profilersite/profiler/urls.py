from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('tasks', views.tasks, name='tasks')
]