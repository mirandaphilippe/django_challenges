from django.db import models

# Create your models here.
class Dimension:
    weight = None
    width = None
    height = None
    length = None

class OrderItem(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    date = models.DateTimeField()
    dimension = Dimension()
    dimension.weight = models.DecimalField(max_digits=4,decimal_places=2)
    dimension.height = models.DecimalField(max_digits=4,decimal_places=2)
    dimension.width = models.DecimalField(max_digits=4,decimal_places=2)
    dimension.length = models.DecimalField(max_digits=4,decimal_places=2)