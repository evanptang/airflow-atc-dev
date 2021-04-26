# Generated by Django 3.1.6 on 2021-02-15 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AirMarshallLogsWithIssueId',
            fields=[
                ('partner_id', models.CharField(blank=True, max_length=100, null=True)),
                ('dag_id', models.CharField(blank=True, max_length=510, null=True)),
                ('dag_url', models.TextField(blank=True, null=True)),
                ('execution_datetime', models.DateTimeField(blank=True, null=True)),
                ('execution_date', models.DateField(blank=True, null=True)),
                ('first_failed_task', models.CharField(blank=True, max_length=510, null=True)),
                ('manual_boolean', models.BooleanField(blank=True, null=True)),
                ('repeated_dag_boolean', models.BooleanField(blank=True, null=True)),
                ('dag_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('dag_start_datetime', models.DateTimeField(blank=True, null=True)),
                ('dag_run_state', models.CharField(blank=True, max_length=100, null=True)),
                ('schedule_interval', models.CharField(blank=True, max_length=100, null=True)),
                ('task_duration', models.IntegerField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('run_id', models.CharField(max_length=255)),
                ('issue_id', models.CharField(max_length=100)),
                ('whitelisted_boolean', models.BooleanField()),
            ],
            options={
                'db_table': 'air_marshall_django_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AirMarshallLogsWithNotes',
            fields=[
                ('partner_id', models.TextField(blank=True, null=True)),
                ('dag_id', models.TextField(blank=True, null=True)),
                ('execution_datetime', models.TextField(blank=True, null=True)),
                ('first_failed_task', models.TextField(blank=True, null=True)),
                ('issue_id', models.TextField(primary_key=True, serialize=False)),
                ('response', models.CharField(blank=True, max_length=300, null=True)),
                ('ticket_id', models.CharField(blank=True, max_length=30, null=True)),
                ('etl_ingestion_time', models.DateTimeField(blank=True, null=True)),
                ('dag_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('resolved', models.BooleanField(blank=True, null=True)),
                ('response_date', models.DateField(blank=True, null=True)),
                ('ticket_to', models.TextField(blank=True, null=True)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL)),
                ('response_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
