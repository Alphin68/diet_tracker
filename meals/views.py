from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal, Food
from .forms import MealForm, FoodForm
from django.contrib import messages

# Create your views here.
def add_meal(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect("list_meal")
    else:
        form = MealForm()
    return render(request,"add_meal.html",{"form":form}) 

def list_meal(request):
    user = request.user
    meal = Meal.objects.filter(user=user)
    return render(request,"list_meal.html",{"meal":meal})  


def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect("list_food")
    else:
        form = FoodForm()
    return render(request,"add_food.html",{"form":form})


def list_food(request):
    user = request.user
    food = Food.objects.filter(user=user)
    return render(request,"list_food.html",{"food":food})


def edit_food(request,id):
    food = get_object_or_404(Food, id = id)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            
            food.save()
            return redirect("list_food")
    else:
        form = FoodForm(instance=food)
    return render(request,"edit.html",{"form":form})


def edit_meal(request,id):
    meal = get_object_or_404(Meal, id = id)
    if request.method == "POST":
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            meal = form.save(commit=False)
            
            meal.save()
            return redirect("list_meal")
    else:
        form = FoodForm(instance=meal)
    return render(request,"edit_m.html",{"form":form})


def delete_meal(request,id):
    meal = get_object_or_404(Meal, id = id)
    meal.delete()
    messages.warning(request, "Deleted meal")
    return redirect('list_meal')

def delete_food(request,id):
    food = get_object_or_404(Food, id = id)
    food.delete()
    messages.warning(request, "Deleted food")
    return redirect('list_food')

