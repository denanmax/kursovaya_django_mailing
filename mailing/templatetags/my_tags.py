from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.filter
def split(text):
    """Обрезает переданный текст до 100 символов"""
    result = text[0:100]
    return mark_safe(result)
