"""Setup script of django-blog-zinnia"""
from setuptools import setup
from setuptools import find_packages

import zinnia

setup(
    name='django-blog-zinnia',
    version=zinnia.__version__,

    description='A clear and powerfull weblog application powered with Django',
    long_description='\n'.join([open('README.rst').read(),
                                open('CHANGELOG').read()]),
    keywords='django, blog, weblog, zinnia, post, news',

    author=zinnia.__author__,
    author_email=zinnia.__email__,
    url=zinnia.__url__,

    packages=find_packages(exclude=['demo']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['beautifulsoup4==4.6.0',
                      'django-contrib-comments==1.8.0',
                      'django-mptt==0.8.7',
                      'django-tagging==0.4.5',
                      'django-xmlrpc==0.1.7',
                      'mots-vides==2015.5.11',
                      'pyparsing==2.2.0',
                      'pytz>=2014.10']
)
