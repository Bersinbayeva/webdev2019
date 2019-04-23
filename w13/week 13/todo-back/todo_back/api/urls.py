from django.urls import path
# from api.views import show_taskLists, show_current_taskList, show_current_tasks
from api.views import TaskLists, TaskListDetail, TaskListTasks, UserList
from api.views import UserList, login, logout
# urlpatterns = [
#     path('task_lists/', show_taskLists),
#     path('task_lists/<int:pk>/', show_current_taskList),
#     path('task_lists/<int:pk>/tasks/', show_current_tasks)
# ]
urlpatterns = [
    path('task_lists/', TaskLists.as_view()),
    path('task_lists/<int:pk>/', TaskListDetail.as_view()),
    path('users/', UserList.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('task_lists/<int:pk>/tasks/', TaskListTasks.as_view())
]