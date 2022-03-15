from django import template

register=template.Library()

@register.filter(name='get_val')

def get_val(dict, key):
    # print(dict.get(key))
    return dict.get(key)