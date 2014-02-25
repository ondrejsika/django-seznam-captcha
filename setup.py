#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-seznam-captcha",
    version = "1.2.2",
    url = 'https://github.com/sikaondrej/django-seznam-captcha/',
    download_url = 'https://github.com/sikaondrej/django-seznam-captcha/',
    license = 'MIT',
    description = "",
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    packages = find_packages(),
    install_requires = ["seznam-captcha"],
    include_package_data = True,
    zip_safe = False,
)
