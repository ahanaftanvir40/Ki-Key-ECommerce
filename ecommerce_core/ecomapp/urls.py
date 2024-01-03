from django.urls import path
from . import views

app_name = 'ecom'
urlpatterns = [
    path('', views.home, name='index'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail')
]
