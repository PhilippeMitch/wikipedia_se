from django.conf import settings

class ArticleWikiRouter:
    def db_for_read(self, model, **hints):
        """
        Les lectures vont à la base de données db_article_wiki
        """
        return 'db_article_wiki'

    def db_for_write(self, model, **hints):
        return 'db_article_wiki'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Les relations entre les objets sont autorisées si les deux objets 
        se trouvent dans l' ensemble db_article / db_titre_wiki.
        """
        db_list = ('db_article_wiki', 'db_titre_wiki')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None



    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Tous les modèles sans article_wiki  se retrouvent dans la 
        base de données db_article_wiki
        """
        return True
