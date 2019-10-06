


"""
Django settings for sp_backend project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from .base import *
MYSQL_HOST = os.environ.get("MARIADB_HOST")
MYSQL_PORT = os.environ.get("MARIADB_PORT")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 14400,
        'NAME': 'emu_master',
        'USER': 'emu_master_user',
        'PASSWORD': '123456',
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.dirname(BASE_DIR)
STATIC_FILE_DIR = os.path.join(SITE_DIR, "static_file")
FILE_PATH_PREFIX = STATIC_ROOT
APP_FOLDER = "app"
SLAVE_PORT = 8000
SCRIPT_FOLDER = "script"
APP_RESC_FOLDER = "app_resc"
