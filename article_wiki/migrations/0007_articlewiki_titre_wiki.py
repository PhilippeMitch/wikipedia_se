# Generated by Django 3.1 on 2020-08-08 17:56

from django.db import migrations
import django.db.models.deletion
import wikipedia_se.crossdb


class Migration(migrations.Migration):

    dependencies = [
        ('titre_wiki', '0003_auto_20200808_1714'),
        ('article_wiki', '0006_remove_articlewiki_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlewiki',
            name='titre_wiki',
            field=wikipedia_se.crossdb.SpanningForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='titre_wiki.titrewiki', verbose_name='Titre'),
        ),
    ]