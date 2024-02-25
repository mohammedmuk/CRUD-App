from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    path('accounts/signup', views.sign_up, name='signup'),
]
