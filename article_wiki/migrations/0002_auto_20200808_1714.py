# Generated by Django 3.1 on 2020-08-08 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_wiki', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WikiArticle',
            new_name='ArticleWiki',
        ),
        migrations.AlterModelTable(
            name='articlewiki',
            table='article_wiki',
        ),
    ]
