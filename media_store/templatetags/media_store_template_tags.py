from django import template
from media_store.models import Category

register = template.Library()

@register.inclusion_tag('media_store/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}