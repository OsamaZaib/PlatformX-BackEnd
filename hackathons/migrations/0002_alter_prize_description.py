# Generated by Django 3.2 on 2021-06-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
