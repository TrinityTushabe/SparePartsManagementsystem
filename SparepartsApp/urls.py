from django.urls import path
#let's import views file from 'SparepartsApp' application
from SparepartsApp import views
#let's reuse the django login view
from django.contrib.auth  import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/<int:product_id>', views.product_detail, name='product_detail'),
    
    
    path('all_sales/', views.all_sales, name='all_sales'),
    path('issued_item/<str:pk>', views.issued_item, name='issued_item'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),
    
    path('add_to_stock/<str:pk>', views.add_to_stock, name='add_to_stock'),
    
    
    path('login/', auth_views.LoginView.as_view(template_name = 'assets/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'assets/index.html'), name= 'logout'),
    
    path('profile/', views.user_profile, name='user_profile'),
        
]