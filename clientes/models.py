from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=68)
    contactado_em = models.DateTimeField(auto_now=True)
    foi_contactado = models.BooleanField(default=False)
