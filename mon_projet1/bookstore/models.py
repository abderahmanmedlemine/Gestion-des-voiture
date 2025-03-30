from django.db import models

# Create your models here.

class membre(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
