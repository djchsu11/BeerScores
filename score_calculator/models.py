from django.db import models


# Create your models here.
class RecipeInput(models.Model):

    def __init__(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])

    OG = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    FG = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    ABV = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    IBU = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    Color = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    BoilSize = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    BoilTime = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    BoilGravity = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    Efficiency = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    PrimaryTemp = models.DecimalField(default=0, decimal_places=5, max_digits=10)
