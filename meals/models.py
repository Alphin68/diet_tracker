from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meal(models.Model):
    TYPE = [('BREAKFAST','BREAKFAST'),('LUNCH','LUNCH'),('SNACK','SNACK'),('DINNER','DINNER')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mealtype = models.CharField(choices=TYPE, max_length=50)

    def __str__(self):
        return f'{self.user.username} - {self.mealtype} on {self.date}'
    

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    protein = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return f'{self.meal.user.username} - {self.name} ({self.meal.mealtype} on {self.meal.date})'