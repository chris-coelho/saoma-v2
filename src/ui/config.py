import os

DEBUG = True
ADMINS = frozenset({
    "cristovao3g@gmail.com"
})

os.environ['APP_ENV'] = 'TEST'  # DEV, TEST, PROD
