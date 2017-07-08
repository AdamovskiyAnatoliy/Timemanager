from django.db import models
from django.utils import timezone


class Note(models.Model):
    class Meta:
        ordering = ['must_complete_before']
    author = models.ForeignKey('auth.User')
    task = models.CharField(max_length=40)
    create_date = models.DateTimeField(default=timezone.now)
    must_complete_before = models.DateTimeField()
    complete_date = models.DateTimeField(default=timezone.now)

    #help_text="Please use the following format: <em>YYYY-MM-DD</em>."
    #class DurationField(**options)
#Поля для хранения периодов времени
    complete_value = models.BooleanField(default=False)

    def complete_task(self):
        self.complete_value = True
        self.complete_date = timezone.now()
        self.save()
        return ''

    def un_complete_task(self):
        self.complete_value = False
        self.save()
        return ''


    def you_have_time(self):
        return self.must_complete_before - timezone.now()



    def __str__(self):
        return self.task
