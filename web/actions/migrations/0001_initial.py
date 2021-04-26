# Generated by Django 3.1.6 on 2021-02-15 20:50

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
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('acknowledge_boolean', models.BooleanField()),
                ('value', models.CharField(max_length=30)),
                ('display_value', models.CharField(max_length=50)),
                ('extended_value', models.CharField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]