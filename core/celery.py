import os
from celery import Celery
from celery.schedules import crontab

# Устанавливаем переменную окружения для Django настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Создаем экземпляр Celery
app = Celery('proj')

# Загружаем конфигурацию Celery из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Определяем задачу для отладки
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'send-payment-reminders-daily': {
        'task': 'app.tasks.send_payment_reminders',
        'schedule': crontab(minute=1),  # Запускать ежедневно в полночь
    },
}

# Автоматически обнаруживаем задачи в приложении
app.autodiscover_tasks()
