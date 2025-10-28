from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/', views.register_view, name='register'),
    path('login/api/',views.LoginAPIView.as_view(), name="login_api"),
    path('message/',views.HelloWorld.as_view(), name="message"),
    path('hello/', views.hello_world, name='hello'),
]
