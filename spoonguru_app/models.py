from django.db import models

# Create your models here.
class ContactRequest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()