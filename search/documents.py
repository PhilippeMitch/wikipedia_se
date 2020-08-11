from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from article_wiki.models import ArticleWiki
from titre_wiki.models import TitreWiki

@registry.register_document
class WikiTitleDocument(Document):
    class Index:
        name = 'titre_wiki'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = TitreWiki

        fields = [
            'id', 'title', 'slug'
        ]


@registry.register_document
class ArticleWikiDocument(Document):
    class Index:
        name = 'article_wiki'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = ArticleWiki

        fields = [
            'id', 'content'
        ]