# Django settings for liberweb project.

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SITE_NAME = 'Libercopy'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql',
        # 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': 'liberweb.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
#    'imdb': {
#        'ENGINE': 'postgresql_psycopg2',
#        'NAME': 'imdb',
#        'USER': 'liberweb',
#        'PASSWORD': 'libre',
#    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'
ugettext = lambda s: s
LANGUAGES = (
 ('es', ugettext('Spanish')),
 ('en', ugettext('English')),
)
TRANSLATION_REGISTRY = 'liberweb.translation'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd#1!3m895ycit%a9pflu%8cmg5llo&0ovnl(_2+h^0qsrn=d0&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'liberweb.invitation.middleware.LoginRequiredMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'liberweb.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'blog/fixtures')
)

INSTALLED_APPS = (
    'localeurl',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'liberweb.serie',
    'liberweb.blog',
    'liberweb.userdata',
    #'liberweb.imdblocal', #Don't use yet, sucks a lot
    'south',
    'modeltranslation',
    'rosetta',
    'sorl.thumbnail',
    'haystack',
    'djangoratings',
    'voting',
    'registration',
    'taggit',
    'django.contrib.comments',
    'avatar',
    'invitation',
)

DATABASE_ROUTERS = ['liberweb.imdblocal.dbrouter.ImdbRouter']

#Valid values are http, sql
IMDB_ACCESS_SYSTEM = "http"  # XXX: sql search is worse

#uri for use with sql
IMDB_ACCESS_DB_URI = "postgres://liberweb:libre@localhost/imdb"

THUMBNAIL_DEBUG = True
THUMBNAIL_SUBDIR = 'thumbs'

if DEBUG:
    try:
        #Check if django-debug-toolbar is installed
        import debug_toolbar
        MIDDLEWARE_CLASSES += (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

        INTERNAL_IPS = ('127.0.0.1',) 

        INSTALLED_APPS += ('debug_toolbar', ) 

        DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False} 
    except: 
        pass 

HAYSTACK_SITECONF = 'liberweb.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'indexes')

# Registration
AUTH_PROFILE_MODULE = 'userdata.UserProfile'
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'
DEFAULT_FROM_EMAIL = 'noreply@libercopy.net'

AUTHENTICATION_BACKENDS = (
    'userdata.models.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#RECAPTCHA_PUBLIC_KEY = '6LfR9L8SAAAAACMxoRCZL5LGLuJYWxFzE6OYds1f'
#RECAPTCHA_PRIVATE_KEY = '6LfR9L8SAAAAAKQiSXtrCZkzlDDhbO0aGob-xuk9'

FORCE_LOWERCASE_TAGS = True

try:
    from local_settings import *
except ImportError:
    pass

# django-invitation
ACCOUNT_INVITATION_DAYS = 7
INVITATIONS_PER_USER = 5

# Si se pone como True, redirige a /accounts/signin
INVITE_MODE = False

LOGIN_EXEMPT_URLS = (
    r'^static/css/*.css', 
    r'^static/js/*.js', 
    r'^static/images/*', 
)

LOGIN_URL_INDEX = '/accounts/signin/'
