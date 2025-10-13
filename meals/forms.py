from django import forms
from .models import Meal, Food


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['mealtype']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','meal','protein','calories']