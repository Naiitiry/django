from django.db import models

# Create your models here.
class Comentarios(models.Model):

    name = models.CharField(max_length=255,null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000,null=True)
    # Si quiero agregar algún campo más, debo ejecutar makemigrations y luego migrate.
    date = models.DateField(null=True)

    def __str__(self):
        return self.name