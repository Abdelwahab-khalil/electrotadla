from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.accuiel, name="accuiel"),
	path('produits/', views.produits, name="produits"),
	path('pc_plazma/', views.pc_plazma, name="pc_plazma"),
	path('electroniques/', views.electroniques, name="electroniques"),
	path('reparation/', views.reparation, name="reparation"),
	path('contact/', views.contact, name="contact"),
    path('detail/<int:id>/', views.detail, name='detail'),
	path("search/", views.search, name="search"),

]