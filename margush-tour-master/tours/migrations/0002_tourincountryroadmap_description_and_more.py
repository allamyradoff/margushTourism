# Generated by Django 4.1 on 2022-08-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourincountryroadmap',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touroutcountryroadmap',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
