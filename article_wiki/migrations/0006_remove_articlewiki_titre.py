# Generated by Django 3.1 on 2020-08-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_wiki', '0005_auto_20200808_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlewiki',
            name='titre',
        ),
    ]
