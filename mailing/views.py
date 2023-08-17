from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from mailing.models import Customer, Message


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
