from django.db import models


class Contact(models.Model):
    """ 
    Model to manage the result processed 
    """
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name
