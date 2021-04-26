from django.db import models
from django.contrib.auth import get_user_model
from actions.models import Action

# Create your models here.
class AirMarshallResponse(models.Model): 
    acknowledged = models.BooleanField() 
    partner_id = models.CharField(max_length=30) 
    airflow_id = models.IntegerField()
    reason = models.CharField(max_length=300)
    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE,
    )
    username = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    issue_id = models.CharField(max_length=75) 
    etl_ingestion_time = models.DateTimeField(auto_now=True)
    dag_id = models.CharField(max_length=300)
    task_id = models.CharField(max_length=300, blank=True, null=True)
    support_notes = models.TextField(blank=True, null=True)
    dag_start_datetime = models.DateTimeField()

    def __str__(self): 
        return self.issue_id 
  