from . import views
from django.urls import path, include


urlpatterns = [
    path('add/',views.add_meal, name="add_meal"),
    path('',views.list_meal, name="list_meal"),
    path('editmeal/<str:id>/',views.edit_meal, name="edit_meal"),
    path('delete/<str:id>/', views.delete_meal, name='delete_meal'),
    path('listmeal/api/',views.ListMealView.as_view(), name="listmeal_api"),


    path('food/',views.add_food, name="add_food"),
    path('list/',views.list_food, name="list_food"),
    path('edit/<str:id>/',views.edit_food, name="edit_food"),
    path('deletefood/<str:id>/', views.delete_food, name='delete_food'),
        
]