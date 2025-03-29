from django.shortcuts import get_object_or_404, redirect, render
from .models import vehicule

# Liste des véhicules
def list(request):
    data_vehi = vehicule.objects.all()
    return render(request, 'list.html', {'data_vehi': data_vehi})

# Ajouter un véhicule
def add(request):
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        modele = request.POST.get('modele')
        dernier_vidange = request.POST.get('dernier_vidange')
        killometrage = request.POST.get('killometrage')
        
        # Vérification que toutes les informations sont présentes
        if matricule and modele and dernier_vidange and killometrage:
            # Assurez-vous que dernier_vidange est une date valide
            data_vehi = vehicule(
                matricule=matricule,
                modele=modele,
                dernier_vidange=dernier_vidange,
                killometrage=killometrage
            )
            data_vehi.save()  
            return redirect('list')  # Rediriger après l'ajout
    
    return render(request, 'list.html')

# Modifier un véhicule
def update(request,matricule):
    vehicule_to_update = get_object_or_404(vehicule, matricule=matricule)
    
    if request.method == 'POST':
        vehicule_to_update.modele = request.POST.get('modele')
        vehicule_to_update.dernier_vidange = request.POST.get('dernier_vidange')
        vehicule_to_update.killometrage = request.POST.get('killometrage')
        
        # Vérification que toutes les informations sont présentes
        if vehicule_to_update.modele and vehicule_to_update.dernier_vidange and vehicule_to_update.killometrage:
            vehicule_to_update.save()  # Sauvegarder les modifications
            return redirect('list')  # Rediriger après la mise à jour
    
    return render(request, 'list.html', {'vehicule': vehicule_to_update})

# Supprimer un véhicule
def delete(request, matricule):
    data_vehicule = get_object_or_404(vehicule, matricule=matricule)
    data_vehicule.delete()  # Supprimer le véhicule
    return redirect('list')  # Rediriger après la suppression
