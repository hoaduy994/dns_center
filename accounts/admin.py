from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]
    fieldsets = (
        ('User', {'fields': ("first_name","last_name","username","email", 'password')}),
        ('Permissions', {'fields': ("is_staff","is_active","is_superuser")}),
        ('Rule', {'fields': ("is_user","is_super","is_admin")}),
    )

    search_fields = ('email','username')
    ordering = ('email','username')

admin.site.register(CustomUser, CustomUserAdmin)