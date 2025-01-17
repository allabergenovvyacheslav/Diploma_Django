from django.urls import path

from .views import *


# '' пробел в кавычках означает главную страницу
urlpatterns = [
    path('', home, name='home'), # Главная страница
    path('products/', product_list, name='product_list'),
    path('contact/', contact_view, name='contact'),
    path('reviews/', reviews_all, name='reviews'),
    path('works/', works_page, name='works'),
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
    path('products/<int:product_id>/reviews/', product_reviews, name='product_reviews'),
    path('website_sign_up/', sign_up_by_website, name='sign_up_by_website'),
    path('api/categories/', category_list_api, name='category_list_api'), # API для категорий
    path('api/products/', product_list_api, name='product_list_api'), # API для товаров
    path('api/products/<int:product_id>/reviews', review_list, name='review_list'), # API для отзывов
]
