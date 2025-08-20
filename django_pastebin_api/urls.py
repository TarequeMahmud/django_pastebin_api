from django.urls import include, path

urlpatterns = [
    path("", include("snippets.urls")),
]
