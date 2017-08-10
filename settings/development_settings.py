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
import sys
from jinja2 import StrictUndefined
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

sys.setrecursionlimit(20000)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mdbtl108v8i0)_q&f$@3j3gie^_^r!xj%-fp-lr@uq)zl0boe%'
APPEND_SLASH = True
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
BASE_URL = 'http://divorcesus.com'
PROFILE_IMAGE_PATH='http://divorcesus.com/static/images/user_no_avatar.png'

ALLOWED_HOSTS = ['divorcesus.com','www.divorcesus.com','127.0.0.1','localhost','www.googleapis.com','https://www.googleapis.com']

SCOPES = ['https://www.googleapis.com/plus/v1/people/me',
          'https://www.googleapis.com/auth/plus.me',
          'https://www.googleapis.com/auth/plus.stream.write']
VERIFY_SSL = False

ADMIN_USERNAME='admin'
SESSION_PROTECTION = 'weak'
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
    'braces',
    'bootstrap3',
    'bootstrap',
    'bootstrap_toolkit',
    'bootstrapform_jinja',
    'clear_cache',
    'encrypted_fields',
    'django_actions',
    'djangobower',
    'django_extensions',
    'django_filters',
    'django_push',
    'django_rq_dashboard',
    'django_rq_jobs',
    'django_rq_email_backend',
    'django_crontab',
    'bootstrap_pagination',
    'drf_cached_instances',
    'facebook',
    'open_facebook',
    'django_user_agents',
    'admin_import',
    'django_jinja',
    'django_jinja2',
    'jinja2',
    'imagekit',
    'favicon',
    'pygments',
    'django_rq',
    'django_wysiwyg',
    'django_social_share',
    'ckeditor',
    'social',
    'social.apps.django_app.default',
    'pyres',
    'hmac',
    'pipeline',
    'redactor',
    'registration',
    'registration_api',
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
    'tastypie',
    'tagging',
    'tinymce',
    'froala_editor',
    'wymeditor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'haystack',
    'channels',
    #'chatrooms',
    #'chat_engine',
    #'polymorphic',
    'oauth2_provider',
    'custom.blog',
    'custom.messaging',
    'custom.feed',
    'custom.users',
    'custom.metaprop',
    'custom.cases',
    'custom.signup',
    'custom.utils',
    'custom.services',
    'custom.chat',
    'custom.chatbot',
    'custom.tasks',
    'custom.gui',
    'custom.payments',
]


SITE_ID=1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
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
            ],

            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
        'SILENTLY_FAIL': True,
    },
}

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
   'options' : {
        'db_table': 'gui_logo',
        'managed': False,
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
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.linkedin.LinkedinOAuth2',
    "allauth.account.auth_backends.AuthenticationBackend",
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
EMAIL_FILE_PATH = '/tmp/email-messages'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'),
                    os.path.join(BASE_DIR, 'static_files/js'), 
                    os.path.join(BASE_DIR, 'static_files/html'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static', )
STATIC_URL = 'http://divorcesus.com/static/'
REGISTRATION_API_ACTIVATION_SUCCESS_URL = '/'
ACTIVATION_HOST = ''
MEDIA_ROOT = './media/'
MEDIA_URL = '/media/'

# See the django-compressor docs at http://django_compressor.readthedocs.org/en/latest/settings/
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False
STATICFILES_DIRS = (
  './static_files',
)


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   # 'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
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
#    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
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

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',   # gets info, Ex. 'name', 'email', etc
    'social.pipeline.social_auth.social_uid',       # gets the uid from the site
    'social.pipeline.social_auth.auth_allowed',     # checks to see if the social is allowed by us. if not will throw a AuthForbidden error
    'social.pipeline.social_auth.social_user',      # checks if the social account is associated in the site
                                                    # and if it is, it returns the user
    'social.pipeline.user.get_username',            # creates a username for the person
                                                    # this is needed to create a unique username if found in DB
    'custom.signup.pipeline.check_duplicate',       # custom method to check for user on other accounts
    'social.pipeline.user.create_user',             # creates a user account if 'user' does not exist yet otherwise returns 'is_new = False'
    'social.pipeline.social_auth.associate_user',   # create the record that associated the social account with this user
                                                    # if for some reason 'social' does not exist but 'user' does
    'social.pipeline.social_auth.load_extra_data',  # Populate the extra_data field in the social record
    'social.pipeline.user.user_details',            # Update the user record with any changed info from the auth service.
                                                    # not sure if we need this but unsure of something that changes data without us knowing
    #'custom.signup.pipeline.save_profile_picture',  # custom method to save profile picture
    'custom.signup.pipeline.consolidate_profiles',   # custom method to delete profile which shouldnt ever occur again
)



SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect'
)

FIELDS_STORED_IN_SESSION = ['key']
FACEBOOK_APPLICATION_ID = '831699350268733'
FACEBOOK_APPLICATION_SECRET_KEY = '0f57b646882a38e45d8a40eb391a1dd0'
FACEBOOK_APPLICATION_NAMESPACE = ''
FACEBOOK_APP_ID = '831699350268733'
FACEBOOK_APP_SECRET = '0f57b646882a38e45d8a40eb391a1dd0'
FANDJANGO_SITE_URL = 'http://divorcesus.com'
SOCIAL_AUTH_TWITTER_KEY = 'scqmosTONSHCvlcxTtLNJR9tF'
SOCIAL_AUTH_TWITTER_SECRET = 'jWWUmos4pRm36En9zmO1UcoUuGMr5GdnatobOdziGwLhwtoVnp'
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77fvb1xbqmead8'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'Ged9hBuDxKakWUZd'
SOCIAL_AUTH_FACEBOOK_KEY = '831699350268733'
SOCIAL_AUTH_FACEBOOK_SECRET = '0f57b646882a38e45d8a40eb391a1dd0'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1021242963135.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'vwfWVtveKrprfuilH01Z_zZK'
SOCIAL_AUTH_INSTAGRAM_KEY = 'e5fe4ae25dfd4d52a7582ed8d61c97c9'
SOCIAL_AUTH_INSTAGRAM_SECRET = '572ccbcf03454dd7bc2c87fa70d77216'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/signin'
SOCIAL_AUTH_LOGIN_URL = '/signin/'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    'access_type': 'offline',
    'approval_prompt': 'auto'
}
#SOCIAL_AUTH_SESSION_EXPIRATION = False
#SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
BROKER_BACKEND                  = "redis"
BROKER_HOST                     = "localhost"
BROKER_PORT                     = 6379
BROKER_VHOST                    = "1"
REDIS_CONNECT_RETRY     = True
REDIS_HOST                              = "localhost"
REDIS_PORT                              = 6379
REDIS_DB                                = "0"
BROKER_URL = 'redis://localhost:6379/0'

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = "default"
RQ_SHOW_ADMIN_LINK = True

# Add a logger for rq_scheduler in order to display when jobs are queueud
LOGGING_CONFIG = None


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend': 'django.core.mail.backends.filebased.EmailBackend',
            'include_html': True,
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'custom': {
            'handlers': ['console','mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'rq_scheduler': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

import logging.config
logging.config.dictConfig(LOGGING)

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


CRONJOBS = [
('*/1 * * * *', 'print "test"'),
('*/1 * * * *', 'python manage.py runtasks'),
('*/1 * * * *', 'artrev.custom.tasks.cron.my_scheduled_job'),
]

_base_main_bundle = (
    'css/reset.css',
    'css/design.css',
)

MEDIA_BUNDLES = (
    ('main.css',)
        + _base_main_bundle,
)
RQ_JOBS_MODULE = 'custom.tasks'
RQ = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': None,
    'socket_timeout': None,
    'connection_pool': None,
    'charset': 'utf-8',
    'errors': 'strict',
    'decode_responses': False,
    'unix_socket_path': None,
}
BOWER_PATH = '/usr/local/bin/bower'
BOWER_COMPONENTS_ROOT = '/var/www/vhosts/divorcesus.com/divorces/'

BOWER_INSTALLED_APPS = (
   'underscore',
   'polymer',
   'webcomponentsjs',
   'gritcode-components',
#   'uglify-js',
)
########## COMPRESSION CONFIGURATION
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
# CSS Files.
#PIPELINE_CSS = {
    # Project libraries.
#    'libraries': {
#        'source_filenames': (   
#            'bower_components/gritcode-components/dist/gritcode-components.css',
#        ),
        # Compress passed libraries and have
        # the output in`css/libs.min.css`.
#        'output_filename': 'css/gritcode.libs.min.css',
#    }
    # ...
#}
# JavaScript files.
#PIPELINE_JS = {
    # Project JavaScript libraries.
#    'libraries': {
#        'source_filenames': (
#            'bower_components/gritcode-components/dist/gritcode-components-bundle.min.js',
#        ),
        # Compress all passed files into `js/libs.min.js`.
#        'output_filename': 'js/gritcode.libs.min.js',
#    }
    # ...
#}
PIPELINE = {
    'PIPELINE_ENABLED': False,
#    'STYLESHEETS': {
#        'colors': {
#            'source_filenames': (
#              'bower_components/gritcode-components/dist/gritcode-components.css',
#            ),
#            'output_filename': 'css/gritcode.css',
#            'extra_context': {
#                'media': 'screen,projection',
#            },
#       },
#    },
#    'JAVASCRIPT': {
#        'stats': {
#            'source_filenames': (
#              'bower_components/gritcode-components/dist/gritcode-components-bundle.min.js',
#            ),
#            'output_filename': 'js/gritcode.js',
#        }
#    }
}

#PIPELINE_YUGLIFY_BINARY = '/usr/local/bin/yuglify'
#PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
#PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor'
#USER_LASTSEEN_TIMEOUT = 300
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

#Cookie name. this can be whatever you want
SESSION_COOKIE_NAME='sessionid'  # use the sessionid in your views code
#the module to store sessions data
SESSION_ENGINE='django.contrib.sessions.backends.db'    
#age of cookie in seconds (default: 2 weeks)
SESSION_COOKIE_AGE= 24*60*60*7 # the number of seconds for only 7 for example
#whether a user's session cookie expires when the web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE=False
#whether the session cookie should be secure (https:// only)
SESSION_COOKIE_SECURE=False
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "./media/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}
TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url', 'video')
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'
REDACTOR_OPTIONS = {'lang': 'en', 'plugins': ['table']}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'ROUTING': 'django_channels.routing.channel_routing',
        'CONFIG': {
            'hosts': [('redis', 6379), ],
        },
    },
}

ADMINS = (
  ('Dmitry', 'dmitryro@gmail.com')
)

#ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value
