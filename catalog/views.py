from django.shortcuts import render
from catalog.models import Product, Category

# Create your views here.


def home(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/home.html')


def catalog(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/catalog.html', context)


def all_products(request, pk):
    product_list = Product.objects.filter(category=pk)
    context = {
        'object_list': product_list,
        'title': 'Все продукты категории'
    }
    return render(request, 'catalog/all_products.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'О продукте'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'catalog/contacts.html', context)
