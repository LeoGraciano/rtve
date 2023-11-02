import os

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db_rtve",
        "USER": "user_rtve",
        "PASSWORD": "password_rtve",
        "HOST": os.environ.setdefault("DB_HOST", "localhost"),
        "PORT": 5432,
    },
}
