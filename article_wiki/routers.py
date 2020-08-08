from django.conf import settings

class ArticleWikiRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to the article_wiki db
        """
        return 'db_article_wiki'

    def db_for_write(self, model, **hints):
        return 'db_article_wiki'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the db_article_wiki database
        """
        db_name = 'db_article_wiki'
        if obj1._state.db == db_name and obj2._state.db == db_name:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non newsletter models end up in the db_article_wiki database
        """
        return True
