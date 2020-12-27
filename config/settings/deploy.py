from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.strip()
    file.close()
    return secret


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret("DJANGO_SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": read_secret("MYSQL_USER"),
        "PASSWORD": read_secret("MYSQL_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}

KAKAO_REST_API_KEY = read_secret("KAKAO_REST_API_KEY")
GH_CLIENT_ID = read_secret("GH_CLIENT_ID")
GH_CLIENT_SECRET = read_secret("GH_CLIENT_SECRET")