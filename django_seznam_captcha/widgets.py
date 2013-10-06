import random

from django import forms
from django.utils.safestring import mark_safe


class CaptchaImageWidget(forms.widgets.Widget):
    def render(self, name, value, attrs={}):
        return mark_safe("""
            <img class="seznam-captcha-img" id="seznam-captcha-img-%(rnd)s">
            <input id="seznam-captcha-key-%(rnd)s" type="hidden" name="%(name)s">
            <script>
            get = function(url){
                var xmlhttp = new XMLHttpRequest();
                xmlhttp.open("GET", url, false);
                xmlhttp.send();
                return xmlhttp.responseText;
            }
            key = get("/seznam-captcha/create/");
            document.getElementById("seznam-captcha-img-%(rnd)s").src = "http://captcha.seznam.cz/captcha.getImage?hash="+key
            document.getElementById("seznam-captcha-key-%(rnd)s").value = key;
            </script>
        """ % {"rnd":random.randint(1000, 9999), "name":name})

class CaptchaInputWidget(forms.widgets.Widget):
    def render(self, name, value, attrs={}):
        return mark_safe("""
            <input class="seznam-captcha-input" type="text" name="%(name)s" value="">
        """ % {"name":name})

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
