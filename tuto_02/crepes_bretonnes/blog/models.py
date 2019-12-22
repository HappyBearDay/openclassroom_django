from django.db import models
from django.utils import timezone


class Categorie(models.Model):
    nom = models.CharField(max_length=30, unique=True,blank=False )

    def __str__(self):
        return self.nom

class Member(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField()
    def __str__(self):
           return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "article"
        ordering = ['date']
        
    def __str__(self):
        return self.titre

