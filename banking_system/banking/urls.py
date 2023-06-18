from django.urls import path  
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('transfer/', views.transfer_money, name='transfer_money'),
    path('transfer/success/', views.transfer_success, name='transfer_success'),
]
