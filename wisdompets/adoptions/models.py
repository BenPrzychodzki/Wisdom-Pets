from django.db import models

class Pet(models.Model): #szablon do naszej bazy danych
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True) #blank=true oznacza, że pozycja nie jest obowiązkowa do wypełnienia
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) #null oznacza, że pozycja może być nieznana
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


