# Generated by Django 3.1.6 on 2021-02-24 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airmarshalllogswithnotes',
            name='response_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response_by', to=settings.AUTH_USER_MODEL),
        ),
    ]