from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_article, name='add_article'),
]