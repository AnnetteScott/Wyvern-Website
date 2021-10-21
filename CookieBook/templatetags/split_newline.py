from django import template

register = template.Library()

@register.filter
def split_newline(value):
    a_list = value.split('\n')
    return a_list