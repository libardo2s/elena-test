from django.contrib.auth.models import User
from django.db import models

STATE_TAKS = ((1, 'Incompleta'), (2, 'Completa'))


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=30, blank=False)
    description = models.CharField('Descripcion', max_length=250, blank=False)
    state = models.CharField('Estado', choices=STATE_TAKS, default=1, max_length=10)
    is_delete = models.BooleanField(default=False)