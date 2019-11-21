from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def call_method(obj, method_name, *args):
    method = getattr(obj, method_name)
    return method(*args)


@register.filter(is_safe=True)
def boolean_icon(value):
    """Prints check, cross or line if True, False or None"""
    if value is True:
        return mark_safe('<i class="fa fa-check"></i>')
    if value is False:
        return mark_safe('<i class="fa  fa-times"></i>')
    if value is None:
        return mark_safe('<i class="fa  fa-minus"></i>')


@register.filter(is_safe=True)
def flag_icon(value):
    value = str(value).lower()
    """Prints check, cross or line if True, False or None"""
    return mark_safe('<span class="flag-icon flag-icon-'+value+'"></span>')
