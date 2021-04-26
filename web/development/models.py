"""Models for Air Marshall Development Work"""
import uuid
from django.db import models
from django.contrib.auth import get_user_model

CURRENT_STATUS = (
    ('unseen','UNSEEN'),
    ('backlog', 'BACKLOG'),
    ('development','DEV'),
    ('finished','FINISHED'),
    ('skipped','SKIP'),
)

# Create your models here.
class DevelopmentTasks(models.Model):
    """
    Model for the Development Tasks
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=CURRENT_STATUS, default='unseen')
    request = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='request'
    )
    response = models.TextField()
    task_image = models.ImageField(upload_to='task_image/', blank=True)
    etl_ingestion_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
