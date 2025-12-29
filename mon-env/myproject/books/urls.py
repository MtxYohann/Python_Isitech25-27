from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_todos_view, name='hello_todos')
]