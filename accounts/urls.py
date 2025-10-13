from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    
]
