# Generated by Django 3.2 on 2021-05-25 20:51

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
                ('name', models.CharField(max_length=80)),
                ('reg_no', models.IntegerField(max_length=50)),
                ('location', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.user')),
                ('education', models.CharField(max_length=80)),
                ('bio', models.CharField(max_length=80)),
                ('lives_in', models.CharField(max_length=80)),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=None)),
                ('interests', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), size=None)),
            ],
        ),
    ]
