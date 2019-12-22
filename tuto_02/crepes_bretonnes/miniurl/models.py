from django.db import models
from django.utils import timezone
# Create your models here.

#url, reduced_url, auteur, compteur, date

class MiniUrl(models.Model):
    url = models.CharField(max_length=250, unique = True)
    reduced_url = models.CharField(max_length=250)
    auteur = models.CharField(max_length=250)
    compteur = models.IntegerField()
    date = models.DateTimeField(default=timezone.now, 
                            verbose_name="Date d'ajout de l'url")

    class Meta:
        verbose_name = "miniurl"
        ordering = ['date']
        
    def __str__(self):
        return self.url
