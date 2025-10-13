from django.contrib import admin
from .models import Meal, Food
# Register your models here.

@admin.register(Meal)

class MealAdmin(admin.ModelAdmin):
    list_display=('user','date','mealtype')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=('meal','name','protein','calories')
 