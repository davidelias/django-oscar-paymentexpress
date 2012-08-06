#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-oscar-paymentexpress',
      version='0.1',
      url='https://github.com/tangentlabs/django-oscar-paymentexpress',
      author="Francis Reyes",
      author_email="francis.reyes@tangentone.com.au",
      description="PaymentExpress payment module for django-oscar",
      long_description=open('README.rst').read(),
      keywords="Payment, PaymentExpress",
      license='BSD',
      packages=find_packages(exclude=['sandbox*', 'tests*']),
      install_requires=['django-oscar>=0.1', ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python']
      )