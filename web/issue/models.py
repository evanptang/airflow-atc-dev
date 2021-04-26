from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class AirMarshallLogsWithIssueId(models.Model):
    dag_id = models.CharField(max_length=510, blank=True, null=True)
    dag_url = models.TextField(blank=True, null=True)
    execution_datetime = models.DateTimeField(blank=True, null=True)
    execution_date = models.DateField(blank=True, null=True)
    first_failed_task = models.CharField(max_length=510, blank=True, null=True)
    manual_boolean = models.BooleanField(blank=True, null=True)
    repeated_dag_boolean = models.BooleanField(blank=True, null=True)
    dag_end_datetime = models.DateTimeField(blank=True, null=True)
    dag_start_datetime = models.DateTimeField(blank=True, null=True)
    dag_run_state = models.CharField(max_length=100, blank=True, null=True)
    schedule_interval = models.CharField(max_length=100, blank=True, null=True)
    task_duration = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    run_id = models.CharField(max_length=255)
    issue_id = models.CharField(max_length=100)
    whitelisted_boolean = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'air_marshall_django_view'

class AirMarshallLogsWithNotes(models.Model):
    dag_id = models.TextField(blank=True, null=True)
    execution_datetime = models.TextField(blank=True, null=True)
    first_failed_task = models.TextField(blank=True, null=True)
    issue_id = models.TextField(null=False, primary_key=True)
    response = models.CharField(max_length=300, blank=True, null=True)
    response_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='response_by',
        null=True,
    )
    ticket_id = models.CharField(max_length=30, blank=True, null=True)
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='reporter'
    )
    etl_ingestion_time = models.DateTimeField(blank=True, null=True)
    dag_end_datetime = models.DateTimeField(blank=True, null=True)
    investigator_resolved = models.BooleanField(blank=True, null=True)
    assignee_resolved = models.BooleanField(default=False, blank=True, null=True)
    response_datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    ticket_to = models.TextField(blank=True, null=True)
