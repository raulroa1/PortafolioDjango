"""
Django settings for portfolioproject project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q3sui31w9+l5a-(&qhplzbq%j_59_%^_6z7+tds3iqej52okdp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myportfolio',
    'bootstrap5',
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = "/uploads/"####   Etapa 4 

# Configuración del idioma predeterminado
LANGUAGE_CODE = 'es'
# Habilita la internacionalización
USE_I18N = True
# Habilita la localización
USE_L10N = True
# Habilita el uso de zonas horarias
USE_TZ = True
# Lista de idiomas disponibles
LANGUAGES = [
    ('es', 'Español'),
    ('en', 'English'),
]
# Ruta a los archivos de traducción
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Configuración de Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "",  # Título del sitio que aparece en la pestaña del navegador.
    "site_header": "Panel de Administrador",  # Encabezado del sitio en el panel de administración.
    "site_brand": "Mi Marca",  # Marca o nombre del sitio que aparece en la barra de navegación.
    "site_logo": "images/logo.png",  # Ruta relativa al logotipo que aparece en la barra de navegación.
    "welcome_sign": "Bienvenido Nombre del programador",  # Mensaje de bienvenida que aparece en la página de inicio de sesión.
    "search_model": "auth.User",  # Modelo utilizado para la búsqueda global en el panel de administración.
    "show_sidebar": True,  # Muestra la barra lateral del menú.
    "navigation_expanded": True,  # Expande la navegación por defecto.
    "order_with_respect_to": ["auth", "books", "book.author", "book.book"],  # Orden de las aplicaciones y modelos en el menú.
    "icons": {  # Iconos para las aplicaciones y modelos específicos.
        "auth": "fas fa-users-cog",  # Icono para la aplicación de autenticación.
        "auth.user": "fas fa-user",  # Icono para el modelo de usuario.
        "auth.Group": "fas fa-users",  # Icono para el modelo de grupos.
    },
    "default_icon_parents": "fas fa-chevron-circle-right",  # Icono por defecto para las aplicaciones principales.
    "default_icon_children": "fas fa-circle",  # Icono por defecto para los modelos dentro de las aplicaciones.
}

# Ajustes de la interfaz de usuario de Jazzmin
JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-white navbar-light",  # Clase CSS para la barra de navegación.
    "theme": "slate",  # Tema de color para el panel de administración.
    "sidebar": "sidebar-dark-primary",  # Clase CSS para la barra lateral.
    "sidebar_nav_child_hide_on_collapse": True,  # Oculta los elementos hijos cuando se colapsa la barra lateral.
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolioproject.urls'

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

WSGI_APPLICATION = 'portfolioproject.wsgi.application'


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

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myportfolio/static')]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myportfolio/static')]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'