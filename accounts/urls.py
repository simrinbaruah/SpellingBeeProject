from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('auth/', include('allauth.urls')),
    path('token_send', views.token, name='token'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('profile', views.profile, name='profile'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('email_sent', views.email_sent, name='email_sent'),
    path('password_reset_done', views.password_reset_done, name='password_reset_done'),
    path('reset/<auth_token>', views.reset, name='reset')
]