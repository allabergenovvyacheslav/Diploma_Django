from django.urls import path
from .views import index


# '' пробел в кавычках означает главную страницу
urlpatterns = [
    path('', index, name='index'),
]
