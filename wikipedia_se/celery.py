import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wikipedia_se.settings')
 
app = Celery('wikipedia_se')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
 
app.conf.beat_schedule = {
    'add-article-every-single-minute': {
        'task': 'article_wiki.tasks.add_article_to_db',
        'schedule': crontab(), 
    },
}