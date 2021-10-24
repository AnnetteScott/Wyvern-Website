from django import template

register = template.Library()

@register.filter
def to_url(value):
    url = value.lower()
    url = url.replace(" ","-")
    return url