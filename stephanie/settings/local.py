from . import base

SECRET_KEY = '!w&sk+%mlnbu^&(lpcja4*93zby!f)4v&+=aj+h6x7*-avomyq'

#INSTALLED_APPS = base.INSTALLED_APPS + ('django_extensions',)
#INSTALLED_APPS = base.INSTALLED_APPS + ('debug_toolbar',)
#MIDDLEWARE_CLASSES = base.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    ('Peter', 'mail@peterbecom'),
)

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG = TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'stephanie',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'gumball',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}


#INSTALLED_APPS = base.INSTALLED_APPS + ('gunicorn',)

#STATIC_URL = '//cdn.peterbecom/'


#import logging
#logging.basicConfig(filename='log.log',
#                    level=logging.DEBUG)

MANAGERS = (
    ('Stephanie', 'stephanie@email.com'),
)
