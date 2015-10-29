# This file is just Python, with a touch of Django which means
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *
from decouple import config

import os.path

CONF_ROOT = os.path.dirname(__file__)

DATA_DIR  = config('SENTRY_DATA_DIR', default='/sentry/data')

DATABASES = {
    'default': {
        'ENGINE':   config('SENTRY_DB_ENGINE', default='django.db.backends.sqlite3'),
        'HOST':     config('SENTRY_DB_HOST',   default=''),
        'PORT':     config('SENTRY_DB_PORT',   default=''),
        'NAME':     config('SENTRY_DB_NAME',   default='/sentry/sentry.db'),
        'USER':     config('SENTRY_DB_USER',   default='postgres'),
        'PASSWORD': config('SENTRY_DB_PASS',   default=''),
    }
}

#########
# Redis #
#########
REDIS_HOST = config('SENTRY_REDIS_HOST', default='redis')
REDIS_PORT = config('SENTRY_REDIS_PORT', default=6379, cast=int)
REDIS_DB   = config('SENTRY_REDIS_DB',   default=0,    cast=int)

# Generic Redis configuration used as defaults for various things including:
# Buffers, Quotas, TSDB

SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': REDIS_HOST,
            'port': REDIS_PORT,
            'db':   REDIS_DB
        }
    }
}

#########
# Cache #
#########

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

#########
# Queue #
#########

# See https://docs.getsentry.com/on-premise/server/queue/ for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

# You can enable queueing of jobs by turning off the always eager setting:
CELERY_ALWAYS_EAGER = config('CELERY_ALWAYS_EAGER', default=False, cast=bool)
CELERY_BROKER_URL   = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)

BROKER_URL = config('SENTRY_BROKER_URL', default=CELERY_BROKER_URL)

###############
# Rate Limits #
###############

# Rate limits apply to notification handlers and are enforced per-project
# automatically.

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

##################
# Update Buffers #
##################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

##########
# Quotas #
##########

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

########
# TSDB #
########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

################
# File storage #
################

# Any Django storage backend is compatible with Sentry. For more solutions see
# the django-storages package: https://django-storages.readthedocs.org/en/latest/

SENTRY_FILESTORE = 'django.core.files.storage.FileSystemStorage'
SENTRY_FILESTORE_OPTIONS = {
    'location': '/sentry/tmp/sentry-files',
}

##############
# Web Server #
##############

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = config('SENTRY_URL_PREFIX' , default='http://sentry.example.com')

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# header and uncomment the following settings
SECURE_PROXY_SSL_HEADER = config('SENTRY_SECURE_PROXY_SSL_HEADER', default=None, cast=lambda x: tuple(x.split(',')) if x else None)

SENTRY_WEB_HOST = config('SENTRY_WEB_HOST', default='0.0.0.0')
SENTRY_WEB_PORT = config('SENTRY_WEB_PORT', default=9000, cast=int)
SENTRY_WEB_OPTIONS = {
    'workers': config('SENTRY_WORKERS', default=3, cast=int),  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

# allows JavaScript clients to submit cross-domain error reports. Useful for local development
SENTRY_ALLOW_ORIGIN = config('SENTRY_ALLOW_ORIGIN', default=None)

###############
# Mail Server #
###############

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND       = config('SENTRY_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST          = config('SENTRY_EMAIL_HOST',    default='localhost')
EMAIL_HOST_USER     = config('SENTRY_EMAIL_USER',    default='')
EMAIL_HOST_PASSWORD = config('SENTRY_EMAIL_PASS',    default='')
EMAIL_PORT          = config('SENTRY_EMAIL_PORT',    default=25,    cast=int)
EMAIL_USE_TLS       = config('SENTRY_EMAIL_USE_TLS', default=False, cast=bool)

# The email address to send on behalf of
SERVER_EMAIL        = config('SENTRY_SERVER_EMAIL', default='root@localhost')

########
# etc. #
########

SENTRY_PUBLIC = config('SENTRY_PUBLIC', default=False, cast=bool)

SENTRY_BEACON = config('SENTRY_BEACON', default=True,  cast=bool)

SENTRY_FEATURES['auth:register'] = config('SENTRY_ALLOW_REGISTRATION', default=False, cast=bool)

SENTRY_ADMIN_EMAIL = config('SENTRY_ADMIN_EMAIL', default='')


# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SECRET_KEY = config('SECRET_KEY', default='5V1r7G3vQBr2gbU2tgDBNitmEuQ82JMtt7N0adHSx2IllzQhRK6HrA==')

# http://twitter.com/apps/new
TWITTER_CONSUMER_KEY      = config('TWITTER_CONSUMER_KEY', default='')
TWITTER_CONSUMER_SECRET   = config('TWITTER_CONSUMER_SECRET', default='')

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID           = config('FACEBOOK_APP_ID', default='')
FACEBOOK_API_SECRET       = config('FACEBOOK_API_SECRET', default='')

# https://github.com/settings/applications/new
GITHUB_APP_ID             = config('GITHUB_APP_ID', default='')
GITHUB_API_SECRET         = config('GITHUB_API_SECRET', default='')

# https://trello.com/1/appKey/generate
TRELLO_API_KEY            = config('TRELLO_API_KEY', default='')
TRELLO_API_SECRET         = config('TRELLO_API_SECRET', default='')

# https://confluence.atlassian.com/display/BITBUCKET/OAuth+Consumers
BITBUCKET_CONSUMER_KEY    = config('BITBUCKET_CONSUMER_KEY', default='')
BITBUCKET_CONSUMER_SECRET = config('BITBUCKET_CONSUMER_SECRET', default='')

