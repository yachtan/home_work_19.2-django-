from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.simple_tag()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '/media/blog/Нет_изображения.jpg'

