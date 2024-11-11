from django.urls import path
from .views import *
from django.contrib.auth import views as reservacni_sys


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("users/users_list", user_list, name="users_list"),
    path("profile/", profile_page, name="profile"),
    path('profile/upravit/', edit_profile, name='edit_profile'),
    path('register/', register_page, name='register'),
    path('login/', helpdesk.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', helpdesk.LogoutView.as_view(template_name='logout.html'), name='logout'),

]