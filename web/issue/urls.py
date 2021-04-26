"""URLs for Issues Application"""
from django.urls import path

from .views import (
    HomeView,
    UnassignedIssuesListView,
    InvestigateListView,
    NotesUpdateView,
    NotesDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('unassigned/', UnassignedIssuesListView.as_view(), name='unassigned_issues'),
    path('investigate/', InvestigateListView.as_view(), name='investigate'),
    path('notes/<str:pk>/edit/', NotesUpdateView.as_view(), name='notes_edit'),
    path('post/<str:issue_id>/', NotesDetailView.as_view(), name='post_detail'),
]
