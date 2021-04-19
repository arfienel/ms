# Generated by Django 3.1.7 on 2021-04-18 10:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newes', '0002_auto_20210418_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='likes',
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(related_name='Лайки', to=settings.AUTH_USER_MODEL),
        ),
    ]
