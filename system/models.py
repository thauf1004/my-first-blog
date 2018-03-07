from django.db import models

class Menu(models.Model):
    menu_id = models.BigIntegerField()
    menu_name = models.CharField ( max_length=200 )
    menu_description = models.TextField()

    def __str__(self):
        return self.menu_name

# Create your models here.