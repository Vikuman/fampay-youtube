from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DEFAULT_SETTINGS_MODULE', 'fampay.settings')

app = Celery('fampay')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery beat settings
app.conf.beat_schedule = {
    'run-every-10-second': {
        'task': 'youtube.tasks.fetch_youtube_videos',
        'schedule': 10
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
