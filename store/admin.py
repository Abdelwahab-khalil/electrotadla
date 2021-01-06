from django.contrib import admin

from .models import Produit, Contact, Demande, Reparation

admin.site.register(Produit)

admin.site.register(Reparation)

admin.site.register(Demande)

admin.site.register(Contact)