from django.contrib import admin
from api.models import TaskList, Task

# admin.site.register(TaskList)
admin.site.register(Task)

@admin.register(TaskList)
class TaskList(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', )
