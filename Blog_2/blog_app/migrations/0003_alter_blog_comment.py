# Generated by Django 3.2.7 on 2022-01-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blog_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
