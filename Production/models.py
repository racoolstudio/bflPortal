from django.db import models


# Create your models here.
class Production(models.Model):
    LITERS_CHOICE = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (10,10),
        (15,15),
        (20,20),
        (25,25)
    ]
    liters = models.DecimalField(max_digits=3,decimal_places=1, choices=LITERS_CHOICE,default=1)
    # blank is used to check if it is required in the frontend while null is for the database
    description = models.TextField(blank=True,null=True)
    total = models.PositiveIntegerField()
    production_date = models.DateField()
