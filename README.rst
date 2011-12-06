django-cms-fancybox
=================
An extension for Django CMS that lets you drop an image or link in a 
placeholder and have it pop up a bigger image or rich text block in
a FancyBox popup.  

Dependancies
============

- django (tested with 1.3)
- django-cms (tested with 2.2)
- django-filer
- django-tinymce (optional)

Getting Started
=============

To get started simply install using ``pip``:
::
    pip install django-cms-fancybox

Add ``cmsplugin_fancybox`` to your installed apps and ``syncdb`` (or migrate, if 
you have south installed).

Your installed apps should look something like this:
::
	INSTALLED_APPS = (
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.sites',
	    'django.contrib.messages',
	    'django.contrib.admin',
	    'tinymce',
        'filer',
        'cms',
	    'cmsplugin_fancybox',
	)

	
Usage
=============

This plugin actually gives you two different types of fancybox plugins, a 
Fancybox Image Popup and a Fancybox Rich Text Popup, with plans for more 
down the road, such as a video popup and an iframe popup.

If you are using a Fancybox Image Popup, just drop the plugin in a Django
CMS placeholder, enter the link text or select a link image from Filer, 
and then select the popup image to display when the link text/image is 
clicked.

If you are using a Fancybox Rich Text Popup, just drop the plugin in a 
Django CMS placeholder, enter the link text or select a link image from 
Filer, and then enter the text to display when the link text/image is 
clicked.  If you have django-tinymce installed it you will be able to enter
rich text, otherwise it's just a text field.


TODO
=============

- Add some optional height/width fields for the Rich Text popup window.
- Add support for a Video Popup
- Add support for an Iframe Popup 
