from django import template
from .. import models,views

register=template.Library()


@register.simple_tag
def user_details(request):
    user = views.user_details_view(request)
    
    return user
