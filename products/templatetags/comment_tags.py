from django import template

register = template.Library()

@register.filter(name='count')
def only_active_comments(comments):
    return comments.count()