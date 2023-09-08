from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from mailing.forms import MessageForm, ClientForm, MailingForm
from mailing.models import Client, Message, Mailing, Log
from mailing.services import send_message_email


class IndexView(TemplateView):
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        return context


# def index(request):
#     mailing_count = Mailing.objects.all().count()
#     active_mailing_count = Mailing.objects.filter(status='started').count()
#     client_count = Client.objects.all().count()
#
#     context = {'title': 'Служба рассылки сообщений',
#                'mailing_count': mailing_count,
#                'active_mailing_count': active_mailing_count,
#                'client_count': client_count}
#     return render(request, 'mailing/index.html', context)


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Наши клиенты'
    }


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:messages')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:messages')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_form_kwargs(self):
        kwargs = super(MailingCreateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            new_mailing = form.save()
            new_mailing.creator = self.request.user
            new_mailing.save()

            if new_mailing.get_status() == 'commenced':
                send_message_email(new_mailing)

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:index')

    def get_form_kwargs(self):
        kwargs = super(MailingUpdateView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class LogListView(ListView):
    model = Log

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset
