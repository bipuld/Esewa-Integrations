from django.db import models
import uuid
# Create your models here.
class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=250)
    
    def __str__(self):
        return self.product_name

class ProductDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    images=models.ImageField(upload_to="product")
    service_charge=models.IntegerField()
    detail=models.TextField()
    price=models.IntegerField(default="")
    token = models.UUIDField(default=uuid.uuid4, editable=False) 
    
    @property
    def tax_price(self):
        return int(self.price * 0.13)
    
    @property
    def total_price(self):
        return self.price + self.service_charge + self.tax_price
    
    def save(self, *args, **kwargs): #token generators
        if not self.token:
            self.token = uuid.uuid4()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{(self.product.pid)} . {self.product.product_name}"
