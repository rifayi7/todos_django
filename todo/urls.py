from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit_todo/<int:id>/', views.edit_todo, name='edit_todo'),
    path('complete_todo/<int:id>/', views.complete_todo, name='complete_todo'), 
]
