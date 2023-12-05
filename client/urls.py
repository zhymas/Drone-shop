from django.urls import path
from .views import LoginUser, RegisterUser

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('sign_up/', RegisterUser.as_view(), name='register')
]