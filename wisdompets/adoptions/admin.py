from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin): #tworzymy nowe okno w ustawieniach administratora, dzieki temu mozemy edytowac nasze informacje o danych zapisanych z modelu Pet
    list_display = ['name', 'species', 'breed', 'age', 'sex'] #aby django nie wyswietlalo informacji pet.object tworzymy liste z informacjami które będziemy chcieli wyświetlać
    
