from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.start),
    path('sign_in', views.sign_in),
    path('pay', views.pay),
    path('regU', views.register_user),
    path('regG', views.regiset_group),
    path('home', views.home),
]