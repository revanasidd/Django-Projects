# Generated by Django 4.0.2 on 2022-02-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='bookissue',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookissue',
            name='book',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookissue',
            name='submit_date',
            field=models.DateField(default=''),
        ),
    ]
