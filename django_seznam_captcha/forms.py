import random

from django import forms
from django.utils.translation import ugettext_lazy as _

import seznam_captcha

from fields import CaptchaField


class CaptchaForm(forms.Form):
    captcha = CaptchaField()

    def clean(self, *args, **kwargs):
        self.cleaned_data = super(CaptchaForm, self).clean(*args, **kwargs)
        if not self.cleaned_data["captcha"]:
            raise forms.ValidationError(_("Bad capcha."))
        return self.cleaned_data