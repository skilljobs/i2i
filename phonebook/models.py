from django.db import models


class Phonebook(models.Model):
    pid = models.CharField(max_length=20)
    name =  models.CharField(max_length=30)
    number =  models.CharField(max_length=50)


    def __str__(self):
        return  self.name + '  ===  ' +self.number 

# Create your models here.
