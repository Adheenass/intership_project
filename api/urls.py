from account.views import  register , login
from doctor.views import doctor
from django.urls import path

urlpatterns = [
    path('register/', register),
    path('login/', login),
]