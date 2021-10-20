from django.shortcuts import render
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', { #pozwala wyrenderowac wiekszy blok html z szablonu ktorego nazwa to home.html
        'pets': pets, #przekazanie zmiennych ktore chcemy wyswietlac
    })

def pet_detail(request, pet_id): #musimy przekazac równiez pet_id, poniewaz uzywamy tej zmiennej przy tworzeniu adresu url
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found') #jesli wpiszemy niepoprawny numer id wtedy wyskoczy blad 404
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })


