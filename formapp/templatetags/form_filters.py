from django import template

register = template.Library()

# クラスを追加するフィルター
@register.filter(name='add_class')
def add_class(value, class_name):
    return value.as_widget(attrs={'class': class_name})
