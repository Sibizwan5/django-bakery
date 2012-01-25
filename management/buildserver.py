import urls
from django.conf import settings
from django.conf.urls.defaults import *
from django.core.management.commands import runserver


class Command(runserver.Command):
    help = "Starts a variation of Django's runserver designed to serve the static files you've built."
    
    def handle(self, *args, **kwds):
        urls.urlpatterns = patterns("toolbox.views",
        url(r"^(.*)$", "static.serve", {
            "document_root": settings.BUILD_DIR,
            'show_indexes': True,
            'default': 'index.html'
            }),
        )
        runserver.Command.handle(self, *args, **kwds)

