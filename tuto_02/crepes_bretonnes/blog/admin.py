from django.contrib import admin
from django.utils.text import Truncator
from .models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
    #Liste des champs du modèle à afficher dans le tableau
    list_display   = ('titre', 'auteur', 'date', "apercu_contenu") 
    #Liste des champs à partir desquels nous pourrons filtrer les entrées
    list_filter    = ('auteur','categorie',)
    #Permet de filtrer par date de façon intuitive
    date_hierarchy = 'date'
    #Tri par défaut du tableau
    ordering       = ('date',)
    #Configuration du champ de recherche
    search_fields  = ('titre', 'contenu')
    
    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['collapse', ],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )


    #Colonne Personnalisée 
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        
        On pourrait le coder nous même, mais Django fournit déjà la 
        fonction qui le fait pour nous !
        """
        return Truncator(article.contenu).chars(40, truncate='...')
    
    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)