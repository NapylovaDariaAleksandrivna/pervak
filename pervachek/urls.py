"""
Нужен для переадресации
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appdatabase.urls'))#Подключает урл из приложения датабэйс
]
 