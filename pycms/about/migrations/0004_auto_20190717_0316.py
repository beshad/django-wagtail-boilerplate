# Generated by Django 2.2.3 on 2019-07-17 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20190717_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='left',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='main',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='right',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
