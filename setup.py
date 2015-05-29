from setuptools import setup

setup(name='datauri',
version='0.0.1',
description='Data URI generator',
long_description='Generates data URIs as defined in RFC 2397, includes command lie utility',
author='Marian Steinbach',
author_email='marian@sendung.de',
url='http://github.com/marians/datauri',
py_modules=['datauri'],
install_requires=['libmagic', 'python-magic', 'click'],
entry_points={
    'console_scripts': [
        'datauri = datauri:main'
    ]
})
