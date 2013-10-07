django-seznam-captcha
=====================

Django wraper for Seznam Captcha

### Authors
*  Ondrej Sika, <http://ondrejsika.com>, ondrej@ondrejsika.com

### Source
* Python Package Index: <http://pypi.python.org/pypi/django-seznam-captcha>
* GitHub: <https://github.com/sikaondrej/django-seznam-captcha>

## Installation

install via pip

    pip install django-seznam-captcha
    
add to root urls

    urlpatterns += url(r'^seznam-captcha/', include('django_seznam_captcha.urls'))


## Usage

use `django_seznam_captcha.fields.CaptchaField`

    from django_seznam_captcha.fields import CaptchaField

    class MyForm(forms.Form):
        usename = forms.CharField()
        captcha = CaptchaField()

or create form from `django_seznam_captcha.forms.CaptchaForm`

    from django_seznam_captcha.forms import CaptchaForm
    
    class MyForm(CaptchaForm):
        username = forms.CharField()

        class Meta:
             fields = ("username", "captcha", )
