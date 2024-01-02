from django.urls import path
from . import views
from ecomapp.views import*

urlpatterns = [
    path = ('', views.index, name ='index')
]
