from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.views import *

app_name = 'mailing'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('mailing', MailingListView.as_view(), name="mailing_list"),
    path('mailing/add', MailingCreateView.as_view(), name='add_mailing'),
    path('mailing<int:pk>/delete', MailingDeleteView.as_view(), name="delete_mailing"),
    path('mailing<int:pk>/edit', MailingUpdateView.as_view(), name="edit_mailing"),
    path('clients', ClientListView.as_view(), name="clients"),
    path('messages', MessageListView.as_view(), name="messages"),
    path('client/add', ClientCreateView.as_view(), name="add_client"),
    path('client<int:pk>/delete', ClientDeleteView.as_view(), name="delete_client"),
    path('client<int:pk>/edit', ClientUpdateView.as_view(), name="edit_client"),
    path('add_message', MessageCreateView.as_view(), name="add_message"),
    path('message<int:pk>/delete', MessageDeleteView.as_view(), name="delete_message"),
    path('message<int:pk>/detail', MessageDetailView.as_view(), name="detail_message"),
    path('message<int:pk>/edit', MessageUpdateView.as_view(), name="edit_message"),
    path('logs', LogListView.as_view(), name="logs"),


]