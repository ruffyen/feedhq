# Django settings for feedhq project.
import os

from django.core.urlresolvers import reverse_lazy

HERE = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Are we running the tests or a real server?
TESTS = False

TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = os.path.join(HERE, os.pardir)
TEST_DISCOVER_ROOT = os.path.join(TEST_DISCOVER_TOP_LEVEL, 'tests')

ADMINS = ()
MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(HERE, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(HERE, 'static')
STATIC_URL = '/static/'

STATICFILES_STORAGE = ('django.contrib.staticfiles.storage.'
                       'CachedStaticFilesStorage')

AUTHENTICATION_BACKENDS = (
    'feedhq.backends.RateLimitMultiBackend',
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
)

ROOT_URLCONF = 'feedhq.urls'

TEMPLATE_DIRS = (
    os.path.join(HERE, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.messages',

    'django_push.subscriber',
    'floppyforms',
    'raven.contrib.django',
    'sekizai',
    'django_rq_dashboard',

    'feedhq.feeds',
    'feedhq.profiles',

    'password_reset',
)

LOCALE_PATHS = (
    os.path.join(HERE, 'locale'),
)

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('feeds:home')

DATE_FORMAT = 'M j, H:i'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'feedupdater': {
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG',
        },
        'ratelimitbackend': {
            'handlers': ['console', 'sentry'],
            'level': 'DEBUG',
        },
        'bleach': {
            'handlers': ['null'],
        },
        'raven': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'sentry.errors': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
