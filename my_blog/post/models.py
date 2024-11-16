from django.db import models
from datetime import date

class Author(models.Model):

    name = models.CharField(max_length=200,null=False)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Entry(models.Model):

    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)

    # # # # # # Clave Foraneas # # # # # #

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    """
    Si se elimina el autor, con CASCADE, se elimina todo lo creado por el mismo.
    """
    # # # # # # # # # # # # # # # # # # #

    def __str__(self):
        return self.headline