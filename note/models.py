from django.db import models



class Note(models.Model):
    masage_note = models.CharField(max_length=200)
    times_call = models.IntegerField(default=1)
    date_call = models.DateTimeField('date call')
    delta_time_call = models.DateTimeField('delta time cole')


    def __str__(self):
        return self.masage_note



# Create your models here.
