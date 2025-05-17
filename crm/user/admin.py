from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'email', 'role', 'status', 'created_at')
    list_filter = ('role', 'status', 'created_at')
    search_fields = ('username', 'full_name', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email')}),
        ('Permissions', {'fields': ('role', 'status')}),
        ('Important dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'password1', 'password2', 'role', 'status'),
        }),
    )

admin.site.register(User, CustomUserAdmin)