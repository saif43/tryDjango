from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title        = models.CharField(max_length=100)
    product_type = models.CharField(max_length=30)
    price        = models.DecimalField(max_digits=10000,decimal_places=2)
    description  = models.TextField(blank=True,null=True)
    available    = models.TextField(default='yes')
    featured     = models.BooleanField(default=True)
    
    # def get_absolute_url(self):
    #     return f'/product/{self.id}'
    

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"p_id": self.id})
    