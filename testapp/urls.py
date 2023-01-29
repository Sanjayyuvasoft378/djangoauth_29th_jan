from pathlib import Path
from django.urls import path
from .views import *
urlpatterns = [

path('register/',RegistrationAPI.as_view(),name='RegistrationAPI'),
path('login/',UserLoginAPI.as_view(),name='UserLoginAPI'),
path('changePassword/',UserChangePasswordAPI.as_view(),name='UserChangePasswordAPI'),
]