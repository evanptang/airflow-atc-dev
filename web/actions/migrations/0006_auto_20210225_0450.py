# Generated by Django 3.1.6 on 2021-02-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0005_auto_20210225_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
