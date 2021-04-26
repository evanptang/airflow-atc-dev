"""URLS for Query API"""
from django.urls import path

from .views import (
    log_issue,
    query_action,
    query_notes_by_issue_id,
    update_action,
    group_by_issue_id,
    calculate_time_difference,
    query_notes_for_response,
    query_users,
    query_aws,
    query_actions_table,
    query_pending_action,
)

urlpatterns = [
    path('log-issue/', log_issue, name='logging'),
    path('queryAction/', query_action, name='query_action'),
    path('queryNotesByIssueId/', query_notes_by_issue_id, name='query_note_by_id'),
    path('updateAction/', update_action, name='update_action'),
    path('groupByIssueId/', group_by_issue_id, name='group_by_issue_id'),
    path('calculateTimeDifference/', calculate_time_difference, name='calculate_time'),
    path('queryNotesResponder/', query_notes_for_response, name='query_responder'),
    path('queryUsers/', query_users, name='query_users'),
    path('queryLastModifiedAWS/', query_aws, name='query_aws'),
    path('getActions/', query_actions_table, name='query_actions'),
    path('queryPendingAction/', query_pending_action, name='query_pending_action')
]
