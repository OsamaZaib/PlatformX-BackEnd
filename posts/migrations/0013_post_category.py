# Generated by Django 3.2 on 2021-07-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default='', max_length=30),
        ),
    ]
