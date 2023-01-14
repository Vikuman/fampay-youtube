from django.apps import AppConfig


class YoutubeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtube'

    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        import fampay.config.celery