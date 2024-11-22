# admin.py
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    # This will display these fields in the list view in the admin panel
    list_display = ('text', 'completed', 'created_at')
    # Enable filtering based on 'completed' and ordering by 'created_at'
    list_filter = ('completed',)
    ordering = ('-created_at',)
    # Enable searching by 'text'
    search_fields = ('text',)

# Register the Todo model with the custom TodoAdmin
admin.site.register(Todo, TodoAdmin)
