from annotationlib import call_annotate_function
from pickle import TRUE
from pyexpat import model
from venv import create

from django.db import models


# tasks/models.py
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Panaderia(models.Model):
    nombre= models.CharField(max_length=100)
    tipo_panes=models.TextField(blank=True)
    utencilios_cocina= models.TextField(blank=TRUE)
    ingredientes= models.TextField(blank=TRUE)
    create_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


    