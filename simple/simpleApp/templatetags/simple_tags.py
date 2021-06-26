from django import template
from simpleApp.models import Author
from django.db.models import Count

register = template.Library()

@register.simple_tag(name='get_authors_list')
def get_authors():
    return Author.objects.all()

@register.inclusion_tag('simpleApp/list_authors.html')
def show_authors():
    # authors = Author.objects.all()
    authors = Author.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    return {'authors': authors}