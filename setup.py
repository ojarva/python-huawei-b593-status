from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='huawei_b593_status',
    version='0.0.1',
    description='Huawei B593 status fetcher',
    long_description=long_description,
    url='https://github.com/ojarva/python-huawei-b593-status',
    author='Olli Jarva',
    author_email='olli@jarva.fi',
    license='BSD',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='huawei 4g b593',
    packages=["huawei_b593_status"],
    install_requires=['xmltodict', 'httplib2'],

    extras_require = {
        'dev': ['twine', 'wheel'],
    },
)
