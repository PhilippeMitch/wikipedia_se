# wikipedia_se
Dans ce projet nous deux applications. Une app titre_wiki qui permet de gérer les titres de wikipedia, et une app article_wiki qui permet de gérer des articles de wikipedia. Ce sont bien deux applications différentes du même projet Django, avec deux bases de données différentes. 


---
Prise en charge de plusieurs bases de données par Django

Mise en place d'un API elasticsearch sur l'une des base données permettant de faire une recherche

## Configuration des bases de données
La base de donnée db_titre_wiki contient initialement les titres de wikipedia français
La base de donnée db_article_wiki contient les articles dont leurs titres sont dans la base de donnée db_titre_wiki

#### La configuration des bases de données pour les deux applications titre_wiki et article_wiki dans le fichier settings.py
```python
 DATABASES = {
    "default": {},
    'db_titre_wiki': {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / 'db_titre_wiki.sqlite3',
    },
    'db_article_wiki': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_article_wiki.sqlite3',
    }   
}
