from django.contrib import admin
from todo.models import TaskList, Task

admin.site.register(TaskList)
admin.site.register(Task)