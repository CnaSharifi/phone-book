# Generated by Django 4.1 on 2022-08-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contactmodel_number1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='number1',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='number2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
