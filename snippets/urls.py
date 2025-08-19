from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetDetail, SnippetList


urlpatterns = [
    path("", SnippetList.as_view()),
    path("<int:pk>/", SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
