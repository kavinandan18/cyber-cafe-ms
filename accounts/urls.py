from django.urls import path
from . import views as account_views

urlpatterns = [
    path('', account_views.LOGIN, name='login'),
    path('register/', account_views.REGISTER, name='register'),
    path('doLogin/', account_views.doLogin, name='doLogin'),
    path('doLogout/', account_views.doLogout, name='logout'),
    path('profile/', account_views.PROFILE, name='profile'),
    path('profile-update/', account_views.PROFILE_UPDATE, name='profile_update'),
    path('change-password/', account_views.CHANGE_PASSWORD, name='change_password'),
]
