from django.urls import path
from .views import *


urlpatterns = [
    path('reminders/', ReminderAPI.as_view(), name='reminders'),
    path('create/', CreateReminderAPI.as_view(), name='create'),
]