# Generated by Django 3.1 on 2020-08-08 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_wiki', '0003_articlewiki_titre_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlewiki',
            name='author',
        ),
        migrations.RemoveField(
            model_name='articlewiki',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='articlewiki',
            name='updated_date',
        ),
    ]
