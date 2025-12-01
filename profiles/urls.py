from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('profile/<int:pk>/', views.profile_page, name='profile'),
    path('search/', views.search_page, name='search'),
]
