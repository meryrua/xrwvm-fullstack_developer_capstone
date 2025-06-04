# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='Ford')
    description = models.TextField()

    # Create a toString method for object string representation
    def __str__(self):
        return self.name + ", " + \
                self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    # dealer_id = models.IntegerField() This brokes dropdown for car model
    # in review page
    name = models.CharField(null=False, max_length=100)
    SEDAN = "sedan"
    SUV = "suv"
    WAGON = "wagon"
    TYPE_CHOISES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon")
    ]
    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOISES,
        default=SEDAN)
    year = models.IntegerField(default=2023,
                            validators=[
                                    MaxValueValidator(2023),
                                    MinValueValidator(2015)
                            ])

    def __str__(self):
        return self.name
