from django import template

register = template.Library()

@register.filter
def percent(value, arg):
    return round((value / arg) * 100, 2)