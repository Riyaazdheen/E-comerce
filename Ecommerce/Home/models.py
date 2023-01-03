from django.db import models

# Create your models here.
def static_dir():
    pass

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=r"F:\Riyaaz\project\E-commerce\Ecommerce\static\assets\product")
    
    def __str__(self) -> str:
        return self.name


class crosel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=r"F:\Riyaaz\project\E-commerce\Ecommerce\static\assets\product")

    def __str__(self) -> str:
        return self.name