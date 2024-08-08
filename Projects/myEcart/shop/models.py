from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    publish_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"
