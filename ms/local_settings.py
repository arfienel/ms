from pathlib import Path
import os,sys
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SECRET_KEY = '&&l7ert(*ykkngst=mw6pg&lj=(qh@+p%!au$j+oyiv1)&@&t5'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
