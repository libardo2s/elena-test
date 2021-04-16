from django.contrib.auth.models import User
from django.db import models

STATE_TAKS = ((1, 'Incompleta'), (2, 'Completa'))


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=30, blank=False)
    description = models.TextField('Description')
    state = models.CharField('State', choices=STATE_TAKS, default=1, max_length=10)
    start_date = models.DateField('Start date', auto_now=True)
    end_date = models.DateField('End date', null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
