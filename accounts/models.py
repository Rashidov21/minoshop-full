from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/',blank=True)
    birthday = models.DateField(blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=150, blank=True)
    zipcode = models.CharField(max_length=150, blank=True)
    # liked_products = models.ManyToManyField(Product, related_name='liked_products')
    
    def __str__(self):
        return self.user.username