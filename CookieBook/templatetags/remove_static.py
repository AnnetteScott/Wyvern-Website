from django import template

register = template.Library()

@register.filter
def remove_static(value):
    value = str(value)
    image_url = value[7:]
    return image_url