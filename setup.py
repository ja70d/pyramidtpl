import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

PROJECT_NAME = 'PYRAMID_TEMPLATE'
DESC = 'THIS IS THE DESCRIPTION'
AUTHOR = 'TBD'
EMAIL = 'TBD@TBD.COM'
ENTRY_POINT = 'TBD:main'

setup(
    name=PROJECT_NAME,
    version='0.1',
    description=DESC,
    long_description=README,
    classifier=[
            'Programming Language :: Python',
            'Framework :: Pyramid',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author=AUTHOR,
    author_email=EMAIL,
    url='',
    keywords='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'paste.app_factory': [
            'main = {}'.format(ENTRY_POINT),
        ],
    },
)
