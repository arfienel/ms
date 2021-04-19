# Generated by Django 3.1.7 on 2021-04-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.PositiveIntegerField(null=True, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='com_author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
    ]
