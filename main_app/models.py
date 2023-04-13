from django.db import models

# Create your models here.
class TeamMember(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name}'