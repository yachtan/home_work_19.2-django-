from django.shortcuts import render

# Create your views here.


def home(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'catalog/contacts.html')
