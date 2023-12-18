from django.contrib import admin
from catalog.models import Category, Product, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'is_active', 'view_count')
    list_filter = ('title',)
    search_fields = ('title', )

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'number', 'is_active')
