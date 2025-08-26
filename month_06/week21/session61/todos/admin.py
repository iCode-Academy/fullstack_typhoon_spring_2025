from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 
                    'completed', 'created_at')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'description')


admin.site.register(Task, TaskAdmin)
