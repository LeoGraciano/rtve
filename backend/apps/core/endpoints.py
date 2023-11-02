from django.urls import include, path
from rest_framework import routers

from apps.accounts import views as accounts_views
from apps.categories import views as categories_views
from apps.expenditure import views as expenditure_views

router = routers.DefaultRouter()
router.register(r"categories", categories_views.CategoryViewSet)
router.register(r"accounts", accounts_views.UserViewSet)
router.register(r"expenditure", expenditure_views.ExpenseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
