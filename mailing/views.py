from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from mailing.models import Customer, Message, Sender, Log


# Create your views here.
class CustomerListView(ListView):
    model = Customer

class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = ('name', 'surname', 'middle_name', 'email', 'comment')
    success_url = reverse_lazy('mailing:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ('name', 'surname', 'middle_name', 'email', 'comment')

    def get_success_url(self):
        return reverse_lazy('mailing:customer_view', kwargs={'pk': self.kwargs['pk']})

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('mailing:customer_list')
##################################


class MessageListView(ListView):
    model = Message

class MessageCreateView(CreateView):
    model = Message
    fields = ('subject', 'message',)
    success_url = reverse_lazy('mailing:message_list')

class MessageDetailView(DetailView):
    model = Message

class MessageUpdateView(UpdateView):
    model = Message
    fields = ('subject', 'message', 'is_active')
    success_url = reverse_lazy('mailing:message_list')

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
##################################


class SenderListView(ListView):
    model = Sender

class SenderCreateView(CreateView):
    model = Sender
    fields = ('frequency', 'status', 'customer', 'message',)
    reverse_lazy = success_url = reverse_lazy('mailing:sender_list')

class SenderUpdateView(UpdateView):
    model = Sender
    fields = ('frequency', 'status', 'customer', 'message',)
    reverse_lazy = success_url = reverse_lazy('mailing:sender_list')

class SenderDeleteView(DeleteView):
    model = Sender
    reverse_lazy = success_url = reverse_lazy('mailing:sender_list')

class LogListView(ListView):
    model = Log



