from threading import Timer
from titre_wiki.models import TitreWiki
from .models import ArticleWiki
import wikipedia

class UpdateArticle(object):

    result = ""

    def _init_(self):
        self.iteration_count = 0
        self.heartbeat = 1    

    @staticmethod
    def add_article(id):
        self.titre_article = TitreWiki.objects.get(pk=id)
        try:
            resume_article = wikipedia.summary(titre_article, sentences=4)
            article_ = ArticleWiki(id=id, content=resume_article, titre_wiki_id=id)
            article_.save(using='db_article_wiki')
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
            


# @app.task
# def add_aticle_to_db():
#     for user in get_user_model().objects.all():
#         posts = Post.objects.filter(author=user)
#         if not posts:
#             continue
 
#         template = Template(REPORT_TEMPLATE)
 
#         send_mail(
#             'Your QuickPublisher Activity',
#             template.render(context=Context({'posts': posts})),
#             'from@quickpublisher.dev',
#             [user.email],
#             fail_silently=False,
#         )