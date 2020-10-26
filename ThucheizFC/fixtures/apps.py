from django.apps import AppConfig


class FixturesConfig(AppConfig):
    name = 'fixtures'

    def ready(self):
        import fixtures.signals
