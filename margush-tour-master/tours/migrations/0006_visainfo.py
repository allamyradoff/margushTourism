# Generated by Django 4.1 on 2022-08-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_rename_file1_bannertourpage_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Информация про Виза',
            },
        ),
    ]
