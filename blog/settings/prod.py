from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_grupo9',
        'USER': 'gtoffa',
        'PASSWORD': 'LCAi@Srs4KG3CnM',
        'HOST': 'gtoffa.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
