# Generated by Django 3.2 on 2021-05-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210524_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='metadata',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
