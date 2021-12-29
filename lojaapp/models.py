from django.db import models

class Categoria(models.Models):
    titulo = models.CharField(max_length=200)
    