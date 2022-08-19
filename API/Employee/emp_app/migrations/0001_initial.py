# Generated by Django 4.0.2 on 2022-02-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
                ('address', models.TextField()),
            ],
        ),
    ]