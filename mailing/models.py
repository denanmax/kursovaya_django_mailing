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


class Sender(models.Model):
    FREQUENCY_CHOICE = (
        ('daily', 'ежедневно'),
        ('weekly', "еженедельно"),
        ('monthly', "ежемесячно")
    )

    STATUS_CHOICE = (
        ('completed', "завершено"),
        ('created', "создано"),
        ('commenced', "запущено")
    )

    commence_time = models.DateTimeField(verbose_name='Время начала рассылки',auto_now_add=True)
    frequency = models.CharField(choices=FREQUENCY_CHOICE, default='daily', verbose_name='Периодичность рассылки')
    status = models.CharField(choices=STATUS_CHOICE, default='created', verbose_name='Статус расссылки')
    customer = models.ManyToManyField(Customer, verbose_name='Клиенты', blank=False)
    message = models.ForeignKey(Message, verbose_name='Письма', on_delete=models.CASCADE, blank=False,
                                limit_choices_to={'is_active': True})

    def __str__(self):
        return f'{self.status}, {self.commence_time}, {self.message}'

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = 'Рассылки'


class Log(models.Model):
    STATUS_CHOICES = [
        ('success', 'успешно'),
        ('failure', 'провал'),
    ]

    sender = models.ForeignKey(Sender, verbose_name='Рассылка', on_delete=models.CASCADE)
    last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки',auto_now_add=True)
    attempt_status = models.CharField(choices=STATUS_CHOICES, verbose_name='Статус попытки')
    server_respond = models.CharField(verbose_name='Ответ сервера')

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = 'Логи'