import random

from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class CaptchaImageWidget(forms.widgets.Widget):
    pass

class CaptchaInputWidget(forms.widgets.Widget):
    pass

class CaptchaWidget(forms.widgets.MultiWidget):
    def __init__(self, *args, **kwargs):
        defaults = {
            'widgets': (
                CaptchaImageWidget(),
                CaptchaInputWidget(),
            )
        }
        defaults.update(kwargs)
        super(CaptchaWidget, self).__init__(**defaults)

    def decompress(self, value):
        return [None, None]

    def render(self, name, value, attrs={}):
        return mark_safe(render_to_string(
            "seznam_captcha/captcha_widget.html",
            {"name":name, }
        ))