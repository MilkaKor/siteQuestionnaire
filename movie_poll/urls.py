from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),  # Перенаправление на опросы для главной страницы
    path('admin/', admin.site.urls),  # Путь для панели администратора
]
