# Generated by Django 3.2.9 on 2022-01-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=200)),
                ('Last_name', models.CharField(max_length=200)),
                ('User_name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=200)),
                ('Password_conform', models.CharField(max_length=200)),
            ],
        ),
    ]
