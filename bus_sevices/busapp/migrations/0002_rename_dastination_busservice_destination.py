# Generated by Django 3.2.7 on 2021-12-24 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busservice',
            old_name='dastination',
            new_name='destination',
        ),
    ]
