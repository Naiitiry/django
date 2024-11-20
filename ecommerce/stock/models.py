from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    short_description=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(blank=False,null=False)
    stock=models.IntegerField(default=20)

    def __str__(self):
        return self.name