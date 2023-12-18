from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='category/', verbose_name='изображение (превью)', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    add_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    change_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=50, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение (превью)', **NULLABLE)
    date_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_active = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
