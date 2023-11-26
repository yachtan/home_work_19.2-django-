from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'pk': 1, 'name': 'огурцы короткоплодные', 'description': 'отличный вкус и весенний аромат',
             'category': Category.objects.get(pk=1), 'price': 350},
            {'pk': 2, 'name': 'тыква', 'description': 'тыква с нежным ароматом и желтой мякотью',
             'category': Category.objects.get(pk=1), 'price': 200},
            {'pk': 3, 'name': 'батат', 'description': 'содержит меньше крахмала, чем картофель',
             'category': Category.objects.get(pk=1), 'price': 300},
            {'pk': 4, 'name': 'томаты черри', 'description': 'очень сладкие',
             'category': Category.objects.get(pk=1), 'price': 380},
            {'pk': 5, 'name': 'яблоки антоновка', 'description': 'местное производство, ароматные и сочные',
             'category': Category.objects.get(pk=2), 'price': 150},
            {'pk': 6, 'name': 'апельсины красные', 'description': 'из Италии',
             'category': Category.objects.get(pk=2), 'price': 350},
            {'pk': 7, 'name': 'груши', 'description': 'местное производство, ароматные',
             'category': Category.objects.get(pk=2), 'price': 290},
            {'pk': 8, 'name': 'кинза', 'description': 'ароматная и свежая',
             'category': Category.objects.get(pk=3), 'price': 100},
            {'pk': 9, 'name': 'базилик', 'description': 'зеленый сорт, отлично подходит для песто',
             'category': Category.objects.get(pk=3), 'price': 180},
            {'pk': 10, 'name': 'проростки подсолнечника', 'description': 'богаты витаминами',
             'category': Category.objects.get(pk=3), 'price': 280},
            {'pk': 11, 'name': 'финики', 'description': 'из Ирана',
             'category': Category.objects.get(pk=4), 'price': 550},
            {'pk': 12, 'name': 'тортик черничный', 'description': 'сыроедный торт со свежей черникой',
             'category': Category.objects.get(pk=4), 'price': 330},
            {'pk': 13, 'name': 'да хун пао', 'description': 'чай красный церемониальный, Китай',
             'category': Category.objects.get(pk=5), 'price': 600},
            {'pk': 14, 'name': 'тегуаньинь', 'description': 'чай улун церемониальный, Китай',
             'category': Category.objects.get(pk=5), 'price': 560},
            {'pk': 15, 'name': 'шпинат', 'description': 'измельченный замороженный',
             'category': Category.objects.get(pk=6), 'price': 340},
            {'pk': 16, 'name': 'облепиха', 'description': 'крупные ягоды',
             'category': Category.objects.get(pk=6), 'price': 380},
            {'pk': 17, 'name': 'кофейный скраб', 'description': 'натуральный состав',
             'category': Category.objects.get(pk=7), 'price': 110}
        ]

        products_to_create = []
        for item in product_list:
            products_to_create.append(Product(**item))

        Product.objects.all().delete()
        Product.objects.bulk_create(products_to_create)
