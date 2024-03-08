from django.db import models


class Reminder(models.Model):
    message = models.CharField(max_length=200, blank=False, null=False)
    reminder_date = models.DateTimeField(blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
