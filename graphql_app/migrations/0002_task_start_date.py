# Generated by Django 3.2 on 2021-04-15 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de inicio de la tarea'),
        ),
    ]
