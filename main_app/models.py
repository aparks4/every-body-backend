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
        return f'{self.date}'


# class Speaker (models.Model):
#     name = models.CharField(max_length=100)
#     image = models.CharField(max_length=250, required=False)
#     description = models.TextField(max_length=500)
#     retreats = # associated Retreat

#     def __str__(self):
#         return f'{self.name}'



