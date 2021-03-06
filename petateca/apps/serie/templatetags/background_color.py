from django import template

register = template.Library()


@register.filter()
def background_color(value):  # Only one argument.
    "Returns color for giving rating"
    rating = value
    if rating > 3: background = 'positive_bg'
    elif rating > 2: background = 'neutral_bg'
    elif rating > 0: background = 'negative_bg'
    elif rating == 0: background = 'no_bg'
    return background
