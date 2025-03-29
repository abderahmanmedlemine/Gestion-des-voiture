from django.db import models

# Create your models here.
class vehicule(models.Model):
    matricule = models.CharField(max_length=100 , verbose_name='matricule')
    modele = models.CharField(max_length=250 , verbose_name='modele')
    dernier_vidange = models.DateField(verbose_name='dernier_vidange')
    killometrage = models.FloatField(verbose_name='killometrage')    

def __str__(self):
        return self.matricule