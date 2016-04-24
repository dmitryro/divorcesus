"""
Django settings for divorces project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/

"""
"""

Django settings for divorces project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from jinja2 import StrictUndefined
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mdbtl108v8i0)_q&f$@3j3gie^_^r!xj%-fp-lr@uq)zl0boe%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['www.googleapis.com','https://www.googleapis.com']

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'admin_tools',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'adminsortable',
    'compressor',
    'bootstrap3',
    'bootstrap',
    'bootstrap_toolkit',
    'bootstrap_pagination',
    'bootstrapform_jinja',
    'clear_cache',
    'encrypted_fields',
    'django_actions',
    'django_filters',
    'django_user_agents',
    'admin_import',
    'django_jinja',
    'django_jinja2',
    'jinja2',
    'favicon',
    'pygments',
    'django_rq',
    'djng',
    'social',
    'social.apps.django_app.default',
    'pyres',
    'redis',
    'redis_cache',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_digestauth',
    'rest_framework_bulk',
    'rest_framework_jwt',
    'rest_framework_oauth',
    'rest_framework_extensions',
    'rest_framework_filters',
    'restless',
    'rules_light',
    'registration_api',
    'tastypie',
    'oauth2_provider',
    'custom.users',
    'custom.metaprop',
    'custom.cases',
    'custom.signup',
    'custom.utils',
    'custom.services',
    'custom.chat',
    'custom.gui',
]


SITE_ID=1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'rules_light.middleware.Middleware',
]

ROOT_URLCONF = 'divorces.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': False,
        'OPTIONS': {
            'loaders': [
                'admin_tools.template_loaders.Loader', 
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django_jinja.loaders.FileSystemLoader',
                'django_jinja.loaders.AppLoader',
                'django_mobile.loader.Loader',
                ('django_mobile.loader.CachedLoader', (
                       'django_mobile.loader.Loader',
                       'django.template.loaders.filesystem.Loader',
                       'django.template.loaders.app_directories.Loader',
                )),
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_DIR = './templates/'
TEMPLATE_DIRS = (
    './templates/',
)


WSGI_APPLICATION = 'divorces.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'divorcesdb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
   },
}

GRAPPELLI_ADMIN_TITLE = 'Divorces US'
GRAPPELLI_CLEAN_INPUT_TYPES = True
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE =  'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_SESSION_LOGIN = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'static', )
STATIC_URL = 'http://divorcesus.com/static/'
REGISTRATION_API_ACTIVATION_SUCCESS_URL = '/'
ACTIVATION_HOST = ''
MEDIA_ROOT = './media/'
MEDIA_URL = '/media/'

COMPRESS_OFFLINE = True
# See the django-compressor docs at http://django_compressor.readthedocs.org/en/latest/settings/
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
STATICFILES_DIRS = (
  './static_files',
)

TEMPLATE_DIRS = [
  './templates/',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

JINJA2_ENVIRONMENT_OPTIONS = {
    'autoescape': False,
    'undefined': StrictUndefined,
}


COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

DEFAULT_AUTHENTICATION = (
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.OAuth2Authentication',
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
     ),
    'DEFAULT_PARSER_CLASSES': (

        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 1000,

    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',

    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
}

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        #'PASSWORD': 'some-password',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'), # If you're on Heroku
        'DB': 0,
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = "default"
RQ_SHOW_ADMIN_LINK = True

# Add a logger for rq_scheduler in order to display when jobs are queueud
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rq_scheduler': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


REST_SESSION_LOGIN = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JINJA2_ENVIRONMENT_OPTIONS = {
    'block_start_string' : '\BLOCK{',
    'block_end_string' : '}',
    'variable_start_string' : '\VAR{',
    'variable_end_string' : '}',
    'comment_start_string' : '\#{',
    'comment_end_string' : '}',
    'line_statement_prefix' : '%-',
    'line_comment_prefix' : '%#',
    'trim_blocks' : True,
    'autoescape' : False,
}

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'



# Same behavior of default intercept method
# by extension but using regex (not recommended)
DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r'.*jinja$'

# More advanced method. Intercept all templates
# except from django admin.
DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r"^(?!admin/).*"



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

JINJA2_ENVIRONMENT_OPTIONS = {
    'block_start_string' : '\BLOCK{',
    'block_end_string' : '}',
    'variable_start_string' : '\VAR{',
    'variable_end_string' : '}',
    'comment_start_string' : '\#{',
    'comment_end_string' : '}',
    'line_statement_prefix' : '%-',
    'line_comment_prefix' : '%#',
    'trim_blocks' : True,
    'autoescape' : False,
    'undefined': StrictUndefined,
}



# Enable/Disable autoescaping (default: True)
JINJA2_AUTOESCAPE = True

# Mute reverse url exceptions (default: False)
JINJA2_MUTE_URLRESOLVE_EXCEPTIONS = True

# Keep original small subset of jinja filters
# instead of use the django's versions of them.
# Default: True
JINJA2_FILTERS_REPLACE_FROM_DJANGO = False

# Enable bytecode cache (default: False)
JINJA2_BYTECODE_CACHE_ENABLE = False

# Cache backend name for bytecode cache (default: "default")
JINJA2_BYTECODE_CACHE_NAME = "default"


JINJA2_CONSTANTS = {
    "email": "dev@artrevolution.com",
}

REACT = {
    'RENDER': not DEBUG,
    'RENDER_URL': 'http://127.0.0.1:8001/render',
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Jingo support
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value
