from django.db import models

# Create your models here.
from django.db import models

# Create your models here.



NULLABLE = {'blank': True, 'null': True}

class Customer(models.Model):
    email = models.EmailField(blank=False, unique=True, verbose_name='почта')
    name = models.CharField(max_length=50, blank=False, verbose_name='имя')
    surname = models.CharField(max_length=50, blank=False, verbose_name='фамилия')
    middle_name = models.CharField(max_length=50, **NULLABLE, verbose_name='отчество (если есть)')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=150, blank=False, verbose_name='Тема Сообщения')
    message = models.TextField(verbose_name='Сообщение')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return f'{self.subject}, {self.pk}'

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = 'Письма'
