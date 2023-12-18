# from django.shortcuts import render
from catalog.models import Product, Category, Blog, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm


class HomeView(TemplateView):
    # главная страница
    template_name = 'catalog/home.html'


class CategoryListView(ListView):
    # страница с каталогом товаров по категориям
    model = Category
    extra_context = {'title': 'Категории товаров', }


class ProductListView(ListView):
    # страница с каталогом продуктов внутри выбранной категории
    model = Product

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        queryset = queryset.filter(category=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        contex_data['title'] = f'Все продукты категории {category_item.name}'
        contex_data['category_pk'] = category_item.pk

        return contex_data


class ProductDetailView(DetailView):
    # просмотр выбранного продукта
    model = Product
    extra_context = {'title': 'О продукте', }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = product_item.category.pk


        version_item = Version.objects.filter(product=product_item.pk, is_active=True).first()

        if version_item:


            context_data['active_version_number'] = version_item.number
            context_data['active_version_name'] = version_item.name
        else:
            context_data['active_version_number'] = 'отсутствует'
            context_data['active_version_name'] = '-'

        return context_data


class ProductCreateView(CreateView):
    # создание продукта
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        contex_data['category_name'] = category_item.name
        return contex_data

    def form_valid(self, form):
        category_pk = self.kwargs['pk']  # Получаем pk категории из URL
        category = Category.objects.get(pk=category_pk)  # Получаем объект категории
        form.instance.category = category  # Устанавливаем категорию для создаваемого продукта
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    # редактирование продукта
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        category_pk = product_item.category.pk
        return reverse('catalog:all_products', args=[category_pk,])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        formset = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    # удаление продукта
    model = Product
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        contex_data['category_pk'] = product_item.category.pk

        return contex_data


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты', }

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'Вы получили сообщение от {name}({phone}): {message}')
        return super().get_context_data(**kwargs)


class BlogListView(ListView):
    # страница с блогами
    model = Blog
    extra_context = {'title': 'Статьи на тему органических продуктов', }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True) # Выводим только активные статьи
        return queryset


class BlogDetailView(DetailView):
    # страница с выбранной статьей
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    # создание статьи
    model = Blog
    fields = ('title', 'content', 'image', )
    success_url = reverse_lazy('catalog:all_blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    # редактирование статьи
    model = Blog
    fields = ('title', 'content', 'image', )
    # success_url = reverse_lazy('catalog:all_blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog', args=[self.kwargs.get('pk'),])


class BlogDeleteView(DeleteView):
    # удаление статьи
    model = Blog
    success_url = reverse_lazy('catalog:all_blogs')

# def contacts(request):
#     context = {
#         'title': 'Контакты'
#     }
#     if request.method == 'POST':
#         # в переменной request хранится информация о методе, который отправлял пользователь
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(name, phone, message)
#
#     return render(request, 'catalog/contacts.html', context)

# def home(request):
#     # создание титульной страницы магазина
#     return render(request, 'catalog/home.html')

# def catalog(request):
#     # страница с каталогом товаров по категориям
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list,
#         'title': 'Категории товаров'
#     }
#     return render(request, 'catalog/category_list.html', context)

# def all_products(request, pk):
#     product_list = Product.objects.filter(category=pk)
#     context = {
#         'object_list': product_list,
#         'title': 'Все продукты категории'
#     }
#     return render(request, 'catalog/product_list.html', context)


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'О продукте'
#     }
#     return render(request, 'catalog/product_detail.html', context)
