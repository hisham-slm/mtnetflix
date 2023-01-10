from django.contrib import admin
from django.urls import path
from . import views
app_name = 'signin'
urlpatterns = [
    path("signin/",views.signin,name='signin_page')
    
]