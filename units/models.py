from django.db import models

# Create your models here.


class Unit(models.Model):
    
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=200, default='Main Avenue 35, Big City')
    description = models.CharField(max_length=256, default='HR')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,related_name='units')
    
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Org Unit"
        ordering = ['name']
    
    
    