# Generated by Django 3.2 on 2021-05-24 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_postvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='entity_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='entity_type',
        ),
        migrations.RemoveField(
            model_name='share',
            name='entity_id',
        ),
        migrations.RemoveField(
            model_name='share',
            name='entity_type',
        ),
        migrations.AddField(
            model_name='image',
            name='metadata',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='image',
            name='path',
            field=models.ImageField(default='', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posts.post'),
            preserve_default=False,
        ),
    ]
