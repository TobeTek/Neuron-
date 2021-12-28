from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'vybz.apps.articles'

    def ready(self) -> None:
        return super().ready()

