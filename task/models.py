from django.db import models
from django.utils import timezone


class Note(models.Model):
    author = models.ForeignKey('auth.User')
    task = models.CharField(max_length=20)
    create_date = models.DateTimeField(default=timezone.now)
    must_complete_before = models.DateTimeField()
    complete_value = models.BooleanField(default=False)

    def complete_task(self):
        self.must_complete_value = True
        self.save()

    def you_have_time(self):
        return self.must_complete_before - timezone.now()


    def __str__(self):
        return self.task
