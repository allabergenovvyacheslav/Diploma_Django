from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import ContactForm, ReviewForm
from .models import Product, Category, Review, Work


# Create your views here.

# Представление для главной страницы
def home(request):
    # Получаем все категории
    categories = Category.objects.all()
    return render(request, 'catalog/home.html', {'categories': categories})


# Создание представления для отображения списка товаров из выбранной категории
def products_by_category(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    return render(request, 'catalog/products_by_category.html',
                  {'category_name': category_name, 'products': products})


# Создание представления для обработки формы обратной связи
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено")
    else:
        form = ContactForm()
    return render(request, 'catalog/contact.html', {'form': form})


# Создание представления для каталога с пагинацией
def product_list(request):
    # Получаем все товары
    products = Product.objects.all()
    # Создаём пагинатор (3 товара на страницу)
    paginator = Paginator(products, 3)
    # Получаем текущую страницу из запроса
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/product_list.html', {'page_obj': page_obj})


# Создание представления для отображения отзывов
def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Если объект не найден, возникает исключение Http404
    reviews = product.reviews.all()  # Получаем все отзывы для продукта

    if request.method == 'POST':  # запрос выполнен с использованием метода POST
        form = ReviewForm(request.POST)
        if form.is_valid():  # проверяет, корректна ли форма
            review = form.save(commit=False)  # возвращает объект, который ещё не сохранён в БД
            review.product = product  # Связываем отзыв с продуктом
            review.save()  # сохраняем
            return redirect('product_reviews', product_id=product.id)  # Перенаправляем на ту же страницу
    else:
        form = ReviewForm()
    return render(request, 'catalog/product_reviews.html',
                  {'product': product, 'reviews': reviews, 'form': form})


def reviews_all(request):
    reviews = Review.objects.all()
    return render(request, 'catalog/reviews_all_products.html', {'reviews': reviews})


# Создание представления регистрации пользователя
def sign_up_by_website(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/') # возвращаемся на главную
    else:
        form = UserCreationForm()
    return render(request, 'catalog/registration_page.html', {'form': form})


def works_page(request):
    works = Work.objects.all()
    return render(request, 'catalog/works_page.html', {'works': works})
