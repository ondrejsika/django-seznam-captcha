import random

from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class CaptchaImageWidget(forms.widgets.Widget):
    def render(self, name, value, attrs={}):
        return mark_safe(render_to_string(
            "seznam_captcha/captcha_image_widget.html",
            {"rnd":random.randint(1000, 9999), "name":name}
        ))

class CaptchaInputWidget(forms.widgets.Widget):
    def render(self, name, value, attrs={}):
        return mark_safe(render_to_string(
            "seznam_captcha/captcha_input_widget.html",
            {"rnd":random.randint(1000, 9999), "name":name}
        ))

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
