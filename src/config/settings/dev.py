import os

from config.settings.base import *  # NOQA

DEBUG = True

CURRENT_ENV = "DEV"

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "HOST": "127.0.0.1",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "PORT": "5432",
        },
    }
else:
    DATABASES = {
        "default_sqlite": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
        # "default_for_local_machine": {
        #     "ENGINE": "django.db.backends.postgresql",
        #     "NAME": "Vasylenko",
        #     "HOST": "localhost",
        #     "USER": "postgres",
        #     "PASSWORD": "admin",
        #     "PORT": "5432",
        # },
    }
