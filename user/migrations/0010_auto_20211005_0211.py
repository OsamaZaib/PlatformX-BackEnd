# Generated by Django 3.2 on 2021-10-04 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_organization_reg_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='github',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='linked_in',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='portfolio',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='twitter',
            field=models.URLField(default=''),
        ),
    ]
