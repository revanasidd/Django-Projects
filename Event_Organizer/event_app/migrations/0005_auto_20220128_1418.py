# Generated by Django 3.2.7 on 2022-01-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0004_auto_20220118_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=1120),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
