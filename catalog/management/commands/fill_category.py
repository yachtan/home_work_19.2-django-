from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'pk': 1, 'name': 'овощи', 'description': 'свежие органические овощи'},
            {'pk': 2, 'name': 'фрукты', 'description': 'свежие органические фрукты'},
            {'pk': 3, 'name': 'зелень', 'description': 'свежая органическая зелень, проростки'},
            {'pk': 4, 'name': 'сладости', 'description': 'полезные сладости'},
            {'pk': 5, 'name': 'чай', 'description': 'чай рассыпной высшего качества, травяные чаи'},
            {'pk': 6, 'name': 'заморозка', 'description': 'замороженные овощи, фрукты, ягоды, зелень'},
            {'pk': 7, 'name': 'косметика', 'description': 'натуральная органическая косметика'},
        ]

        category_to_create = []
        for item in category_list:
            category_to_create.append(Category(**item))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_to_create)
