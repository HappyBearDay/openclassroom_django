from django.contrib import admin
from .models import MiniUrl

#url, reduced_url, auteur, compteur, date

class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'reduced_url',
    'auteur', 'compteur', 'date')
    list_filter = ('auteur', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('url', )

admin.site.register(MiniUrl, MiniURLAdmin)