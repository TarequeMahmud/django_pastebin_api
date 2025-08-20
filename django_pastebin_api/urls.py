from django.urls import include, path


from django_pastebin_api.accounts import views


urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("snippets.urls")),
]
