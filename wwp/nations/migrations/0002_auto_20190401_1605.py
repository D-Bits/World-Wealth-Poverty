# Generated by Django 2.2 on 2019-04-01 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financial',
            old_name='gdp_per_captia',
            new_name='gdp_per_capita',
        ),
    ]
