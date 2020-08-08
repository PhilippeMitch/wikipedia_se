from django.db import models

# Create your models here.
class ArticleWiki(models.Model):

    content = models.TextField()
    author = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='article_wiki'

    def save(self):
        super(ArticleWiki, self).save()