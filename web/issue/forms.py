from django import forms
from django.contrib.auth import get_user_model
from .models import AirMarshallLogsWithNotes


class SignupForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        max_length=35,
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        max_length=35,
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class NotesForm(forms.ModelForm):
    class Meta:
        model = AirMarshallLogsWithNotes
        exclude = [
            "partner_id",
            "dag_id",
            "first_failed_task",
            "execution_datetime",
            "reporter",
            "ticket_to",
            "issue_id",
            "dag_end_datetime",
            "etl_ingestion_time",
            "response_datetime",
            "response_by"
        ]