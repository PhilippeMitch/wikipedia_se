from django.conf import settings

"""
Nous voulons un routeur qui envoie toutes les applications qui n'ont pas
app_label = 'titre_wiki' à la base de données db_titre_wiki
"""

class TitreWikiRouter:
    """
    Un routeur pour contrôler toutes les opérations sur les modèles dans le
    application titre_wiki
    """

    def db_for_read(self, model, **hints):
        """
        Les tentatives de lecture des modèles titre_wiki vont à db_titre_wiki
        """
        if model._meta.app_label == 'titre_wiki':
            return 'db_titre_wiki'
        return None

    def db_for_write(self, model, **hints):
        """
        Les tentatives d'écriture dans les modèles titre_wiki vont à db_titre_wiki
        """
        if model._meta.app_label == 'titre_wiki':
            return 'db_titre_wiki'
        return None


    def allow_relation(self, obj1, obj2, **hints):
        """
        Autoriser les relations uniquement si obj1._meta.app_label == obj2._meta.app_label
        """
        app_label_name = 'titre_wiki'
        #Si les deux modèles ont app_label = 'titre_wiki' autoriser la relation entre eux
        if obj1._meta.app_label == app_label_name and \
        obj2._meta.app_label == app_label_name:
            return True
        #au prochain routeur
        elif app_label_name not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

        #Else - un modèle a app_label = 'titre_wiki' l'autre pas -
        #Forbid une relation couvrant plusieurs bases de données - non pris en charge dans Django
        else:
            return False


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Assurez-vous que l'application titre_wiki n'apparaît que dans le 'db_titre_wiki'
        """

        if db == 'db_titre_wiki':
            return app_label == 'titre_wiki'

        elif app_label == 'titre_wiki':
            return False
        return None