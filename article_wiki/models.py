from django.db import models
from titre_wiki.models import TitreWiki
from wikipedia_se.crossdb import SpanningForeignKey

# Create your models here.
class ArticleWiki(models.Model):

    titre_wiki = SpanningForeignKey(TitreWiki, on_delete=models.CASCADE, default=None, null=True, blank=True, verbose_name='Titre')
    content = models.TextField()


    class Meta:
        db_table='article_wiki'

    # @property
    # def titre_wiki(self):
    #     return TitreWiki.objects.get(pk=self.id)

    def save(self):
        super(ArticleWiki, self).save()