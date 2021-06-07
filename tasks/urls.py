from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.get, name='get'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
]
