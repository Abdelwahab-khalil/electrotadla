from django.db import models
from django.db.models.fields import EmailField

class Produit(models.Model):
    nom = models.CharField(max_length=50)
    petite_description = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    plus_information = models.CharField(max_length=500)
    categorie = models.CharField(max_length=50)
    prix  = models.IntegerField()
    stock = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    picture_1 = models.URLField()
    picture_2 = models.URLField()
    picture_3 = models.URLField()
    picture_4 = models.URLField()
    picture_5 = models.URLField()
    picture_6 = models.URLField()

    def __str__(self):
        return self.nom

class Reparation(models.Model):
    nom = models.CharField(max_length=50)     
    email = models.CharField(max_length=50)   
    tele = models.CharField(max_length=50)    
    module = models.CharField(max_length=50)    
    probleme = models.CharField(max_length=200)  
    prix = models.IntegerField()

    def __str__(self):
        return self.nom

class Contact(models.Model):
    nom = models.CharField(max_length=50)     
    email = models.CharField(max_length=50)   
    tele = models.CharField(max_length=50)    
    message = models.CharField(max_length=200)  

    def __str__(self):
        return self.nom     

class Demande(models.Model):
    nom_produit = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)     
    tele = models.CharField(max_length=50)  
    address = models.CharField(max_length=100, default="address" )
    message = models.CharField(max_length=200)  

    def __str__(self):
        return self.nom                 

       