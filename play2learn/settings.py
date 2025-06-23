import os
from pathlib import Path
from django.conf import settings
import dj_database_url

def global_debug(request):
   return{'debug': settings.DEBUG}

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0^=_l^slk4l=b236-2q9+)5om$ge)%ovmz%@^fltsu)sgnww41'

DEBUG = False

# Don't use local host but still keep it, kept all local host references in settings.py
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "play2learn-lmn4.onrender.com",
    "play2learn.app",
    "www.play2learn.app",
]

# APPS SECTION
INSTALLED_APPS = [
   # built-in django apps
   'django.contrib.admin',
   'django.contrib.admindocs',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'django.contrib.sites',
   'django_extensions',
   'django_password_eye',

   # local apps
   'pages.apps.PagesConfig',
   'contact.apps.ContactConfig',
   'users.apps.UsersConfig',
   'reviews.apps.ReviewsConfig',

   # third-party apps
   'crispy_forms',
   'crispy_bootstrap5',
   'allauth',
   'allauth.account',
   'allauth.socialaccount',
   'storages',
   'games',
   'scoreboards',
   'corsheaders',
   'widget_tweaks',
]

# changed from 1 since host name was changed then changed it again (now it's 3)
SITE_ID = 3 

# CRISPY SECTION
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# MIDDLEWARE SECTIONS
MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
   'django.contrib.admindocs.middleware.XViewMiddleware',
   'django.middleware.cache.CacheMiddleware',
   'allauth.account.middleware.AccountMiddleware',
   'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'play2learn.urls'

SESSION_COOKIE_NAME = 'sessionid'  # default name, make sure it’s this or adjust frontend accordingly
SESSION_COOKIE_DOMAIN = '.play2learn.app'  # make sure this includes your frontend domain so the cookie is accessible
SESSION_COOKIE_PATH = '/'  # usually root, to be accessible site-wide
SESSION_COOKIE_SAMESITE = 'Lax'  # or 'None' with HTTPS
SESSION_COOKIE_SECURE = True  # true if using HTTPS, false otherwise


# TEMPLATES SECTION
TEMPLATES = [
   {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [
           os.path.join(BASE_DIR, 'templates'),
           os.path.join(BASE_DIR, 'templates/vue-templates')
       ],
       'APP_DIRS': True,
       'OPTIONS': {
           'context_processors': [
               'play2learn.settings.global_debug',
               'django.template.context_processors.debug',
               'django.template.context_processors.media',
               'django.template.context_processors.request',
               'django.contrib.auth.context_processors.auth',
               'django.contrib.messages.context_processors.messages',
               'django.template.context_processors.tz',
               'play2learn.context_processors.vue_games_cdn',
           ],
       },
   },
]

# Time zone is one hour behind without this (I'm not sure why)
TIME_ZONE = 'America/New_York'
USE_TZ = True

WSGI_APPLICATION = 'play2learn.wsgi.application'

# EMAIL SECTION
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = 'neeneez2008@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_FORMS = {
    'signup': 'users.signup_form.CustomSignupForm',
}

# DATABASES SECTION

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://zoe:Pandora117!@localhost:5432/play2learn'
    )
}

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

# AUTHENTICATION SETTINGS
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

## ALLUTH SETTINGS settings
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_SIGNUP_REDIRECT_URL = 'pages:homepage'
ACCOUNT_AUTHENTICATED_REDIRECT_URL = 'pages:homepage'
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_RATE_LIMITS = {
   "login_failed": "5/m"  # limits attempted login for 5 minutes (safety / security)
}

AUTHENTICATION_BACKENDS = (
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
)

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_TZ = True

# CLOUDFRONT SETTINGS

VUE_GAMES_CDN_URL = 'https://d247zk0j19bbkg.cloudfront.net/static/vue-games'


# AWS SETTINGS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'play2learn-bucket'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_QUERYSTRING_AUTH = True
AWS_S3_REGION_NAME = 'us-east-2'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'play2learn.storage_backends.PublicMediaStorage'
PRIVATE_FILE_STORAGE = 'play2learn.storage_backends.PrivateMediaStorage'
STATIC_URL = 'https://play2learn-bucket.s3.us-east-2.amazonaws.com/static/'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com/media/public/'
PUBLIC_MEDIA_LOCATION = 'media/public'
PRIVATE_MEDIA_STORAGE = 'media/private'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'no-cache, no-store, must-revalidate',
} # website caches a lot without this, also put in some different .py files for website

STATICFILES_DIRS = [
   BASE_DIR / 'static',  
]
STATIC_ROOT = None
STORAGES = {
   "default": {
       "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
   },
   "staticfiles": {
       "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
   },
   "private_files": {
       "BACKEND": "play2learn.storage_backends.PrivateMediaStorage",
   },
}

CORS_ALLOWED_ORIGINS = [
   "http://localhost:8080",  
   "http://localhost:8000",
   "https://www.play2learn.app",
   "https://play2learn.app",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJANGO_PASSWORD_EYE_INCLUDE_FONT_AWESOME = False

CSRF_COOKIE_HTTPONLY = False
CSRF_TRUSTED_ORIGINS = ['https://www.play2learn.app']


try:
   if os.environ.get('ENVIRONMENT') != 'production':
      from .local_settings import *
except ImportError:
   pass
# DON'T PUT ANYTHING BELOW THIS