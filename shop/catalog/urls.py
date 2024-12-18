from django.urls import path

from .views import *


# '' пробел в кавычках означает главную страницу
urlpatterns = [
    path('', home, name='home'), # Главная страница
    path('products/', product_list, name='product_list'),
    path('contact/', contact_view, name='contact'),
    path('reviews/', reviews_all, name='reviews'),
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
    path('products/<int:product_id>/reviews/', product_reviews, name='product_reviews'),
]
