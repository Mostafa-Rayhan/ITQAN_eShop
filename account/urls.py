from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),

    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/search/', views.search, name="search"),
    path('products/<slug:product_name>/', views.selected_product, name="selected product"),

]