from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import CustomerListView, CustomerDetailView, CustomerUpdateView, CustomerCreateView, \
    CustomerDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = MailingConfig.name





urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('create_customer/', CustomerCreateView.as_view(), name='create_customer'),
    path('view/<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
    path('edit/<int:pk>/', CustomerUpdateView.as_view(), name='edit_customer'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('create_message', MessageCreateView.as_view(), name='create_message'),
    path('message<int:pk>/view', MessageDetailView.as_view(), name="message_view"),
    path('message<int:pk>/edit', MessageUpdateView.as_view(), name="edit_message"),
    path('message<int:pk>/delete', MessageDeleteView.as_view(), name="delete_message"),
]