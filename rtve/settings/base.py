from .middleware_settings import *  # noqa: ignore=F401 isort:skip
from .installed_apps_settings import *  # noqa: ignore=F401 isort:skip
from .internationalizations_settings import *  # noqa: ignore=F401 isort:skip
from .auth_settings import *  # noqa: ignore=F401 isort:skip
from .host_settings import *  # noqa: ignore=F401 isort:skip
from .media_settings import *  # noqa: ignore=F401 isort:skip
from .email_settings import *  # noqa: ignore=F401 isort:skip
from .rest_framework_settings import *  # noqa: ignore=F401 isort:skip
from .cache_settings import *  # noqa: ignore=F401 isort:skip
from .database_settings import *  # noqa: ignore=F401 isort:skip


# from .django_select2_settings import *  # noqa: ignore=F401 isort:skip

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

DJANGO_SETTINGS_MODULE = "rtve.settings.base"

ROOT_URLCONF = "rtve.urls"

WSGI_APPLICATION = "rtve.wsgi.application"

ASGI_APPLICATION = "rtve.asgi.application"

NAME_SYSTEM = "CETT URG"

IS_SIGNAL = True
# CSRF_FAILURE_VIEW = 'core.views_errors.csrf_failure'
