# Generated by Django 3.2 on 2021-11-24 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sphere_engine', '0004_submission_fyp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='fyp',
        ),
    ]
