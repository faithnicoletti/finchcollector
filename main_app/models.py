from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    habitat = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    diet = models.CharField(max_length=100)

#Changing this instance method
# does not impact the datbase, therefore
# no migration needs to be made

def __str__(self):
    return f'{self.name} ({self.id})'