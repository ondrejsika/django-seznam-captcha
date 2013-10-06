import random

from django import forms

import seznam_captcha

from widgets import CaptchaWidget


class CaptchaField(forms.MultiValueField):
    def __init__(self, **kwargs):
        defaults = {
            'widget': CaptchaWidget(),
            'fields': (
                forms.CharField(max_length=32),
                forms.CharField(max_length=32),
            )
        }
        defaults.update(kwargs)
        super(CaptchaField, self).__init__(**defaults)

    def clean(self, value, *args, **kwargs):
        key, code = value
        return seznam_captcha.check(key, code)