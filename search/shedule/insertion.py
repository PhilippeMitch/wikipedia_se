from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from search import views

def start():
        scheduler = BackgroundScheduler()
        scheduler.add_job(views.home, 'interval', minutes=1)
        scheduler.start()