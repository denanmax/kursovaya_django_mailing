from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from mailing.models import Mailing, Log
from django.utils import timezone


def send_message_email(mailing: object) -> None:
    try:
        send_result = send_mail(mailing.message.subject,
                  mailing.message.text,
                  settings.EMAIL_HOST_USER,
                  list(
                      mailing.clients.values_list('email', flat=True)
                  )
                  )
    except:
        send_result = False
    now = timezone.now()
    if send_result:
        log_status = 'success'
    else:
        log_status = 'failed'
    log = Log.objects.create(mailing=mailing, last_attempt=now, status=log_status)
    log.save()


def send_mailing():
    now = timezone.now()
    mailing_list = Mailing.objects.exclude(status='completed')
    for mailing in mailing_list:
        if mailing.get_status() == 'commenced':
            last_send = mailing.log_set.filter(status='success').order_by('-last_attempt').first()
            if last_send:
                if mailing.frequency == 'daily':
                    send_time = last_send.last_attempt + timedelta(days=1)
                elif mailing.frequency == 'weekly':
                    send_time = last_send.last_attempt + timedelta(days=7)
                else:
                    send_time = last_send.last_attempt + timedelta(days=30)
                if (send_time - now) < timedelta(minutes=15):
                    send_message_email(mailing)
            else:
                send_message_email(mailing)




