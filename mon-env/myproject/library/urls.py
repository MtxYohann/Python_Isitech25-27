from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_library_view, name='library'),
    path('list', views.library_list, name='library_list')
]