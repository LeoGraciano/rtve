BUSINESS_APPS = [
    "apps.accounts",
    "apps.core",
    "apps.categories",
    "apps.expenditure",
]

THIRD_APPS = [
    "bootstrap5",
    "rest_framework",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + BUSINESS_APPS  # AWGI server
