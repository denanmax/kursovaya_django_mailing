from django.db import models

from django.utils import timezone

NULLABLE = {"null": True, "blank": True}


class Client(models.Model):
    email = models.CharField(max_length=200, verbose_name='E-mail')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=250, verbose_name='Тема', default='Рассылка')
    text = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Mailing(models.Model):
    FREQUENCY_CHOICE = (
        ("daily", "день"),
        ("weekly", "неделя"),
        ("monthly", "месяц"),
    )

    STATUS_CHOICE = (
        ("created", "Создана"),
        ("completed", "Завершена"),
        ("commenced", "Запущена"),
    )

    commence_time = models.DateTimeField(verbose_name='Старт рассылки')
    completion_time = models.DateTimeField(verbose_name='Завершение рассылки')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICE, default='day',
                                   verbose_name='Периодичность')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='created', verbose_name='Статус')
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')

    def get_status(self):
        now = timezone.now()
        if self.commence_time < now < self.completion_time:
            self.status = "commenced"
        elif now > self.completion_time:
            self.status = "completed"
        self.save()
        return self.status

    def __str__(self):
        return f'{self.message}: {self.frequency}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Log(models.Model):
    STATUS_CHOICE = (
        ("success", "Исполнена"),
        ("failed", "Провалена"),
    )
    mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', on_delete=models.CASCADE)
    last_attempt = models.DateTimeField(verbose_name='Время последней попытки')
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, verbose_name='Статус попытки')

    def __str__(self):
        return f'{self.mailing} ({self.last_attempt}) - {self.status}'

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
