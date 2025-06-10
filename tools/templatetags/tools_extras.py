from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def pretty_event_date(value):
    if not value:
        return ""
    now = timezone.localtime(timezone.now())
    # Make value timezone-aware if it's naive
    if timezone.is_naive(value):
        value = timezone.make_aware(value, timezone.get_current_timezone())
    value = timezone.localtime(value)
    delta = value.date() - now.date()
    if delta.days == 0:
        return value.strftime("%H:%M")
    elif 0 < delta.days < 7:
        return value.strftime("%A %H:%M")
    else:
        return value.strftime("%d/%m")

@register.filter
def rating(back_odds, lay_odds):
    try:
        return (float(back_odds) / float(lay_odds)) * 100 if lay_odds else None
    except (ValueError, ZeroDivisionError, TypeError):
        return None