from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Animal(models.Model):
    nombre = models.CharField(max_length=50)
    
    fecha_nacimiento = models.DateField()
    continentes = {
        'Europa':"Europa",
        'Africa':'Africa',
        'America del Sur':'America del Sur',
        'America del Norte':'America del Norte',
        'Oceania':'Oceania',
        'Antartica':'Antartica'
    }
    continente = models.CharField( max_length=20,
                  choices=continentes,
                  default="Africa")
    
    pais = models.CharField(max_length=20)
    especie = models.ForeignKey('Especie', on_delete=models.CASCADE, blank=True, related_name = "especie_nombre")
    zoo = models.ForeignKey('Zoo',on_delete=models.CASCADE,blank=True,related_name="nombreZoo")
    
    
    def __str__(self):
        return self.nombre 
    
    
    
class Especie(models.Model):
    sexos = {
        'H':'Hembra',
        'M':'Macho'
    }
    
    posible_extincion = {
        'Si': True,
        'No':False
    }
    
    nombre_cientifico = models.CharField(max_length=25,primary_key=True)
    nombre_comun = models.CharField(max_length=25,blank=True)
    extincion = models.BooleanField(choices=posible_extincion,blank=True)
    familia = models.CharField(max_length=25,blank=True)
    def __str__(self):
        return self.nombre_cientifico
    
    
class Zoo(models.Model):
    nombre = models.CharField(max_length=25,blank=True)
    ciudad = models.CharField(max_length=25,blank=True)
    pais = models.CharField(max_length=25,blank=True)
    presupuesto = models.FloatField(blank=True)
    tamañoMetrosCuadrado = models.FloatField(blank=True ,verbose_name="Espacio")
    
    def __str__(self):
        return self.nombre
    
    
    

    
    
    
    