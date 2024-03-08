from .models import Reminder
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import ReminderSerializer


class ReminderAPI(generics.ListAPIView):
    queryset = Reminder.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ReminderSerializer

class CreateReminderAPI(generics.CreateAPIView):
    queryset = Reminder.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ReminderSerializer