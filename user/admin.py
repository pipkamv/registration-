from django.contrib import admin
from .models import UserModels

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'is_active']
    list_display_links = ['id', 'first_name', 'last_name', 'username']
    list_filter = ['is_active']
    search_fields = ['email', 'first_name', 'last_name']

    class Meta:
        model = UserModels


admin.site.register(UserModels, MyUserAdmin)

