from django.conf import settings

"""
We want a router that sends all the apps that don't have an
app_label='titre_wiki' to the db_titre_wiki database
"""

class TitreWikiRouter:
    """
    A router to control all operations on models in the
    titre_wiki application
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read titre_wiki models go to db_titre_wiki
        NOTE: model._meta.app_label is the name of the respective app
        so it might be titre_wiki or posts or auth or contenttypes or w/e if it's 
        django default or 3rd party app
        """
        if model._meta.app_label == 'titre_wiki':
            return 'db_titre_wiki'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write to titre_wiki models go to db_titre_wiki
        """
        if model._meta.app_label == 'titre_wiki':
            return 'db_titre_wiki'
        return None


    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relationships only if obj1._meta.app_label == obj2._meta.app_label
        """
        app_label_name = 'titre_wiki'
        #If both models have app_label = 'titre_wiki' allow relation between them
        if obj1._meta.app_label == app_label_name and \
        obj2._meta.app_label == app_label_name:
            return True
        #to next router
        elif app_label_name not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

        #Else - one model has app_label = 'titre_wiki' the other one does not -
        #Forbid a relationship spanning multiple databases - not supported in Django
        else:
            return False


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the titre_wiki app only appears in the 'db_titre_wiki'
        """

        if db == 'db_titre_wiki':
            return app_label == 'titre_wiki'

        elif app_label == 'titre_wiki':
            return False
        return None