from django.contrib.auth.models import User
from django.db import models

STATE_TAKS = ((1, 'Incompleta'), (2, 'Completa'))


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=30, blank=False)
    description = models.TextField('Descripcion')
    state = models.CharField('Estado', choices=STATE_TAKS, default=1, max_length=10)
    start_date = models.DateField('Fecha de inicio de la tarea', auto_now=True)
    end_date = models.DateField('Fecha de finalizacion de la tarea', null=True, blank=True)
    is_delete = models.BooleanField(default=False)
