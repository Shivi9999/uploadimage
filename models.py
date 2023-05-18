from django.db import models

# Create your models here.
class Multiple(models.Model):
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(default="")
    contact=models.CharField(max_length=12,default="")
    images=models.FileField()
    def __str__(self):
        return self.name
    