from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def show_size(size, as_plain_text=False):
    try:
        w, h, d = size
    except ValueError:
        w, h = size
        d = None

    def _show_centimeters(cm):
        return "%d cm" % cm

    def _show_imperial(cm):
        inches = 0.393700787401575 * cm
        feet = cm * 3.2808399 / 100
        inches = (feet * 12) % 12
        feet = int(feet)
        if feet > 0:
            return u"%d'%d\u2033" % (feet, int(inches))
        else:
            return u'%.1f\u2033' % inches

    first = [
        _show_centimeters(w),
        _show_centimeters(h)
    ]
    second = [
        _show_imperial(w),
        _show_imperial(h),
    ]
    if d is not None:
        first.append(_show_centimeters(d))
        second.append(_show_imperial(d))

    if as_plain_text:
        template = "%(first)s (%(second)s)"
    else:
        template = '<abbr title="%(second)s">%(first)s</abbr>'

    return mark_safe(template % (
         dict(first=' x '.join(first),
              second=' x '.join(second))
    ))
