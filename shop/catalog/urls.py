from django.urls import path
from .views import product_list, home, contact_view

# '' пробел в кавычках означает главную страницу
urlpatterns = [
    path('', home, name='home'), # Главная страница
    path('products/', product_list, name='product_list'),
    path('contact/', contact_view, name='contact'),
]
