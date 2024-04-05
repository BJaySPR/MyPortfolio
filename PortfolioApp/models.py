from django.db import models

# Create your models here.
class Send_messate(models.Model):
    name= models.CharField(max_length =200)
    email =models.EmailField()
    message=models.CharField(default = False, max_length=254)

    def __str__(self):
        return self.name
    
