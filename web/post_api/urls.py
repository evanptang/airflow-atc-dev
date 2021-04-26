from django.urls import path

from .views import (
    modify_support_notes,
    remove_response,
    upsert_into_notes,
    create_note_if_none,
    approve_action,
)

urlpatterns = [
    path('updateSupportNotes/', modify_support_notes, name='modify'),
    path('removeResponse/', remove_response, name='remove_response'),
    path('updateAssignee/', upsert_into_notes, name='upsert'),
    path('createNoteIfDoesNotExist/', create_note_if_none, name='create_note_if_none'),
    path('approveAction/', approve_action, name='approve_action'),
]
