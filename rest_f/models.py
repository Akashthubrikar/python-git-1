from django.db import models

class cast(models.Model):
    name = models.CharField(max_length=100)
    school= models.CharField(max_length=200)


    def __str__(self):
       return self.name + " " +self.school