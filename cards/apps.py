from django.apps import AppConfig


class CardsConfig(AppConfig):
    name = 'cards'

    def ready(self):
        from prices import updater
        updater.start()