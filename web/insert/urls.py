from django.urls import path

from .views import (
    ResponseSearchListView,
    IgnoreSearchListView,
)

urlpatterns = [
    path('assignment/', ResponseSearchListView.as_view(), name='response_search'),
    path('ignoreIssues/', IgnoreSearchListView.as_view(), name='ignore_issues'),
]