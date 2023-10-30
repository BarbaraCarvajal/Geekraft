from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')

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
    'rest_framework', #Api
    'rest_framework_simplejwt.token_blacklist', #autenticación
    'users', #app de usuarios
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'backend.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #Carpeta donde se guardan los archivos estáticos
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'dist/static')
] 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #Carpeta donde se guardan los archivos multimedia  

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'users.User' #Modelo personalizado de usuario

CORS_ALLOWED_ORIGINS = [
  'http://localhost:5173'
] #Permitir peticiones desde este origen

CORS_ALLOWED_CREDENTIALS = True #Permitir credenciales

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50), #Tiempo de vida del token de acceso
  'REFRESH_TOKEN_LIFETIME': timedelta(minutes=50), #Tiempo de vida del token de refresco
  'ROTATE_REFRESH_TOKENS': True, #Rotar tokens de refresco
  'BLACKLIST_AFTER_ROTATION': True, #Bloquear tokens de refresco anteriores
  'UPDATE_LAST_LOGIN': False, #Actualizar última fecha de inicio de sesión

  'ALGORITHM': 'HS256', #Algoritmo de encriptación
  'VERIFYING_KEY': SECRET_KEY, #Llave de verificación
  'AUDIENCE': None, #Audiencia
  'ISSUER': None, #Emisor
  'JWK_URL': None, #URL de llave pública
  'LEEWAY': 0, #Margen de error

  'AUTH_HEADER_TYPES': ('Bearer',), #Tipos de cabecera de autenticación
  'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION', #Nombre de cabecera de autenticación
  'USER_ID_FIELD': 'id', #Campo de id de usuario
  'USER_ID_CLAIM': 'user_id', #Reclamo de id de usuario
  'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule', #Regla de autenticación de usuario

  'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), #Clases de token de autenticación
  'TOKEN_TYPE_CLAIM': 'token_type', #Reclamo de tipo de token
  'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser', #Clase de usuario de token

  'JTI_CLAIM': 'jti', #Reclamo de identificador único

}

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
  ),
}
