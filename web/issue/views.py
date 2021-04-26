"""Views for Issue App"""
from datetime import timedelta, datetime
import pytz

from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.urls import reverse_lazy

from .models import AirMarshallLogsWithIssueId, AirMarshallLogsWithNotes
from .forms import NotesForm


class HomeView(ListView):
    model = AirMarshallLogsWithIssueId
    template_name = 'issue/home.html'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-dag_start_datetime')


class NotesDetailView(UpdateView):
    model = AirMarshallLogsWithNotes
    template_name = 'issue/note_detail.html'
    fields = '__all__'

    def get_object(self, queryset=None):
        return AirMarshallLogsWithNotes.objects.get(issue_id=self.kwargs.get("issue_id"))


@method_decorator(login_required, name='dispatch')
class UnassignedIssuesListView(ListView):
    model = AirMarshallLogsWithIssueId
    template_name = 'issue/unassigned_issues.html'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        hour_filter = self.request.GET.get('hourfilter', None)
        utcnow = pytz.utc.localize(datetime.utcnow())
        issues = AirMarshallLogsWithIssueId.objects.order_by(
            '-dag_start_datetime')
        if hour_filter is not None:
            try:
                hour_filter = int(hour_filter)
                datetime_hours_ago = utcnow - timedelta(hours=hour_filter)
                issues = issues.filter(
                    dag_start_datetime__range=(datetime_hours_ago, utcnow)        
                )
            except:
                pass
        if query is not None:
            issues = issues.filter(
                Q(dag_id__icontains=query) |
                Q(first_failed_task__icontains=query) |
                Q(partner_id__icontains=query)
            )
        return issues


@method_decorator(login_required, name='dispatch')
class InvestigateListView(ListView):
    model = AirMarshallLogsWithNotes
    template_name = 'issue/investigate_issues.html'
    paginate_by = 25

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        hour_filter = self.request.GET.get('hourfilter', None)
        utcnow = pytz.utc.localize(datetime.utcnow())
        issues = AirMarshallLogsWithNotes.objects.order_by(
            '-execution_datetime').filter(response_by=self.request.user)
        if hour_filter is not None:
            try:
                hour_filter = int(hour_filter)
                datetime_hours_ago = utcnow - timedelta(hours=hour_filter)
                issues = issues.filter(
                    dag_start_datetime__range=(datetime_hours_ago, utcnow)        
                )
            except:
                pass
        if query is not None:
            issues = issues.filter(
                Q(dag_id__icontains=query) |
                Q(first_failed_task__icontains=query) |
                Q(partner_id__icontains=query)
            )
        return issues



@method_decorator(login_required, name='dispatch')
class NotesUpdateView(UpdateView):
    model = AirMarshallLogsWithNotes
    form_class = NotesForm
    template_name = 'issue/note_edit.html'
    success_url = reverse_lazy('investigate')

    def form_valid(self, form):
        form.instance.response_by = self.request.user
        return super().form_valid(form)
