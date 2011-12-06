from setuptools import setup, find_packages
import os

version = __import__('cmsplugin_fancybox').__version__

install_requires = [
    'setuptools',
    'django',
    'django-cms',
    'django-filer',
    'django-tinymce',
]

setup(
    name = "django-cms-fancybox",
    version = version,
    url = 'http://github.com/megamark16/django-cms-fancybox',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "A fancybox extension for Django CMS",
    author = "Mark Ransom",
    author_email = 'megamark16@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'cmsplugin_fancybox': 'cmsplugin_fancybox',
    },
)
