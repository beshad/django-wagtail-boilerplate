from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0dy14@khgw4eq791bbaj+1z41zijdz$a%%#0!9j533b)2^+9t_'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

# Uncomment this line to enable template caching
# Dont forget to change the LOCATION path
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": "/path/to/your/site/cache"
#     }
# }

try:
    from .local import *
except ImportError:
    pass
