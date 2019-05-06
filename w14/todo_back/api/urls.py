from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    #path('tasklist/', views.tasklists),
    #path('tasklist/<int:pk>/', views.tasklist_detail),
    #path('tasklist/<int:pk>/tasks', views.tasks_of_tasklist),
    #path('tasklist/', views.TaskLists.as_view()),
    #path('tasklist/<int:pk>/', views.TaskListDetail.as_view()),
    #path('tasklist/<int:pk>/tasks/', views.TasksOfTaskList.as_view()),
    path('tasklist/', views.TaskLists.as_view()),
    path('tasklist/<int:pk>/', views.TaskListDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)
]