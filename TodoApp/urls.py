from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
   
    path('',views.home,name='home'),
    path('add-todo/',views.add_todo,name='add-todo'),
    path('delete-todo/<int:todoId>/', views.delete_todo, name='delete-todo'),
]
