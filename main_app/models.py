from django.db import models

# Create your models here.
class TeamMember(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


class Retreat (models.Model):

    name = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    description = models.TextField(max_length=2500, null=True, blank=True)
    image = models.CharField(max_length=250)
    # itinerary = 
    # speakers =
    registrationURL = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    
class ResourceCategory (models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Resource (models.Model):

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=120)
    description = models.TextField(max_length=1200, null=True, blank=True)
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'



