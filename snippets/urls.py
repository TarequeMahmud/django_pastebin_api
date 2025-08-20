from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# register api viewsets
router = DefaultRouter()

router.register(r"snippets", viewset=views.SnippetViewSet, basename="snippet")
router.register(r"users", viewset=views.UserViewSet, basename="user")


# API endpoints
urlpatterns = [
    path("", include(router.urls)),
]
