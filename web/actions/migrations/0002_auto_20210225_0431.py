# Generated by Django 3.1.6 on 2021-02-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='pending_confirmation',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]