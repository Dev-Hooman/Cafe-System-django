from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
    