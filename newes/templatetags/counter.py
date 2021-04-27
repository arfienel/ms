from django import template
from newes.models import PageHit


register = template.Library()


@register.simple_tag(takes_context=True)
def page_hits(context, page_url=None):
    if page_url:
        page_url = f'/{page_url}/'
    counter = (PageHit.objects
                      .filter(url=(context['request'].path if page_url is None else page_url))
                      .first())
    return 0 if counter is None else counter.count