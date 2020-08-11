from threading import Timer
from titre_wiki.models import TitreWiki
from .models import ArticleWiki
import wikipedia
# from background_task import background

class UpdateArticle(object):

    result = ""

    def _init_(self):
        self.iteration_count = 0
        self.heartbeat = 60    

    @staticmethod
    def add_article(id):
        self.titre_article = TitreWiki.objects.get(pk=id)
        try:
            resume_article = wikipedia.summary(self.titre_article, sentences=4)
            article_ = ArticleWiki()
            article_._state.adding = False
            article_._state.db = 'db_article_wiki'
            article_.content = resume_article
            article_.titre_wiki = id
            article_.save()
        except wikipedia.exceptions.DisambiguationError as e:
            for options in e.options:
                error += options.decode("utf-8","ignore")+'\n'
        except wikipedia.exceptions.PageError:
            error = "Aucun message n'a pu être trouvé avec le sujet que vous avez entré!"

    def start_job(self):
        self.add_article(self.iteration_count)
        self.iteration_count += 1

        timer = Timer(
            interval=self.heartbeat,
            function=self.start_job,
        )

        timer.start()

        if self.iteration_count >= 100:
            timer.cancel()
            

# @background(schedule=60)
# def notify_user():
#     for titre_wiki in TitreWiki().objects.all():
#         titre_wiki_ = TitreWiki.objects.filter(title=titre_wiki_)
#         if not titre_wiki:
#             continue


# @app.task
# def add_aticle_to_db():
#     for titre_wiki in TitreWiki().objects.all():
#         titre_wiki_ = TitreWiki.objects.filter(title=titre_wiki_)
#         if not titre_wiki:
#             continue
 
#         template = Template(REPORT_TEMPLATE)
 
