# Generated by Django 4.2.4 on 2023-08-18 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_remove_sender_customer_sender_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sender',
            name='customer',
        ),
        migrations.AlterField(
            model_name='sender',
            name='message',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='Письма'),
        ),
        migrations.AddField(
            model_name='sender',
            name='customer',
            field=models.ManyToManyField(to='mailing.customer', verbose_name='Клиенты'),
        ),
    ]
