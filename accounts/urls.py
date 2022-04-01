from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('auth/', include('allauth.urls')),
    path('token_send', views.token, name='token'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('profile', views.profile, name='profile')
]