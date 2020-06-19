from django.apps import AppConfig


class UserpageConfig(AppConfig):
    name = 'userpage'

    def ready(self):
        import userpage.signals