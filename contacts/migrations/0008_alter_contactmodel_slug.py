# Generated by Django 3.2.13 on 2022-09-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20220901_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
    ]
