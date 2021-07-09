import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '&&l7ert(*ykkngstbsrbsdfbsrg%faf@dd=mw6pg&lj=(qh@+p%!au$j+oyiv1)&@&t5'
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
