import requests

from django.http import HttpResponse


def create_view(request):
    return HttpResponse(requests.get("http://captcha.seznam.cz/captcha.create").text)

def check_view(request, key, code):
    return HttpResponse(requests.get("http://captcha.seznam.cz/captcha.check?hash=%s&code=%s"%(key, code)).text)
