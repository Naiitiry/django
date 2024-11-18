from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()

    # La vinculacion de 1 a muchos va en la FK y del lado que son muchos, es decir los articulos.
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline