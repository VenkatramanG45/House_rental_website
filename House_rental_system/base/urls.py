# rental/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('listings/', views.listings, name='listings'),
    path('add/', views.add_property, name='add_property'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    
    path('register/', views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('booking/<int:property_id>/', views.booking, name='booking'), 
    # Add more URL patterns as needed
]
