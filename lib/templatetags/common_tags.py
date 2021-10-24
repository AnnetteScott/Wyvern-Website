from django import template

register = template.Library()

@register.filter
def to_url(value):
    url = value.lower()
    url = url.replace(" ","-")
    return url

@register.filter
def remove_static(value):
    value = str(value)
    image_url = value[7:]
    return image_url

@register.filter
def split_newline(value):
    a_list = value.split('\n')
    return a_list