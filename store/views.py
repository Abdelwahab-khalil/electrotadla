from store.models import Contact, Demande, Produit, Reparation
from django.shortcuts import render


def accuiel(request):

     produits = Produit.objects.all() 

     context = {
           'produits': produits
     }
     return render(request, 'store/accueil.html', context)
     
def produits(request):

     produits = Produit.objects.all() 

     context = {
           'produits': produits
     }
     return render(request, 'store/produits.html', context)


def detail(request,id):

      produit = Produit.objects.get(id=id)

      if request.method == 'POST':
        nom = request.POST.get('nom')
        tele = request.POST.get('tele')
        address = request.POST.get('address')
        message = request.POST.get('message')
        demande = Demande.objects.create(
            nom_produit = produit.nom,
            nom = nom,
            tele=tele,
            address = address,
            message=message

        )  
        demande.save()
        return render(request, 'store/merci.html')
      
      context = {
            'produit': produit
      }
      return render(request, 'store/detail.html', context)


def pc_plazma(request):
      
     produits = Produit.objects.filter(categorie = 'pc_plasma') 

     context = {
           'produits': produits
     }
     return render(request, 'store/pc_plazma.html', context)    


def electroniques(request):

     produits = Produit.objects.filter(categorie = 'electroniques') 

     context = {
           'produits': produits
     }
     return render(request, 'store/electroniques.html', context) 


def reparation(request):
      if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        tele = request.POST.get('tele')
        module = request.POST.get('module')
        probleme = request.POST.get('probleme')
        rep = Reparation.objects.create(
            nom = nom,
            email = email,
            tele=tele,
            prix = 0,
            module=module,
            probleme=probleme

        )  
        rep.save()
        return render(request, 'store/merci.html')
        
      context = {}
      return render(request, 'store/reparation.html', context) 

def contact(request):
      if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        tele = request.POST.get('tele')
        message = request.POST.get('message')
        contact = Contact.objects.create(
            nom = nom,
            email = email,
            tele=tele,
            message=message

        )  
        contact.save()
        return render(request, 'store/merci.html')
      context = {}
      return render(request, 'store/contact.html', context)   

def search(request):
    query = request.GET.get('search')
    if not query:
        produits = Produit.objects.all()
    else:
        produits = Produit.objects.filter(nom__icontains=query)

    message = "Résultats %s" % query
    context = {
        'produits': produits,
        'nom': message
    }
    return render(request, 'store/search.html', context)      

         