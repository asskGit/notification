from celery import shared_task
from django.utils import timezone
from .models import Transaction


@shared_task
def send_payment_reminders():
    today = timezone.now().date()
    transactions_due = Transaction.objects.filter(date_transfer=today, status='Не оплачен')

    for transaction in transactions_due:
        user = transaction.user
        notification_message = f'Ваша транзакция с ID {transaction.id} не была оплачена.'

        user.notifications.append({
            'transaction_id': transaction.id,
            'message': notification_message,
            'date': timezone.now().isoformat()
        })
        user.save()