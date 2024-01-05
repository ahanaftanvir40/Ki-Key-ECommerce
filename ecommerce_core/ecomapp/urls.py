from django.urls import path
from . import views

app_name = 'ecom'
urlpatterns = [
    path('', views.home, name='index'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('category/<str:foo>', views.category, name= 'category' ),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
