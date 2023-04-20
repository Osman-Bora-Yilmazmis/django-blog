
import os
from pathlib import Path

#BURASI SETTINGS KISMIDIR DJANGO'nun kalbi burasıdır. uygulama için ayarlara buradan erişilebilir.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ecqqiwvgbu=%=qq@@=c&6ik_%36-w5jria6-h46si18guod))='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',#blog dosyası
    'account',#account dosyası
    # third party
    'ckeditor',# ck editör admin panelinde yazı üzerinde customize yapmamızı sağlar
    'crispy_forms', # iletişim html'sinde kullandık UI ekranını güzelleştiriyor
    "crispy_bootstrap4",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],#sayfa kalıtımı için app dışındaki templates klasörüne erişmesini sağladık çünkü
        'APP_DIRS': True,                 #Bazı özellikler (navbar, menü, login ekranı gibi özellikler aynı olduğu için kod tekrarını önler)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'tr' #TURKCE DIL DESTEGI

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


STATICFILES_DIRS = [  #harici static oluşturucaksak (app dışından js dosyaları css dosyaları)
    BASE_DIR / "static" #static dosyasına erişmemimizi sağlar
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.CustomUserModel' #account dosyası içinde default olarak verilen user'a avatar ekleyip güncelledikten sonra sisteme AUTH_USER_MODEL tablosunda değişiklik yaptıırdık.

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/') #Media klasörünün yolunu girdik.

CRISPY_ALLOWED_TEMPLATE_PACKS = "Bootstrap4" #crispy kutuphanesi icin

CRISPY_TEMPLATE_PACK = "Bootstrap4" #crispy kutuphanesi icin

LOGIN_REDIRECT_URL = '/' #kullanici giriş ekranındaki bilgilerini doldurup gönderince otomatik olarak anasayfa ekranına yönlendirilir