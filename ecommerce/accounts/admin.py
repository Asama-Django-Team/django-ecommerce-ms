from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserChangeForm

from .models import User


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = ("email", "phone_number", "full_name", "is_admin")
    list_filter = ("is_admin", "is_active")
    readonly_fields = ("last_login",)

    add_fieldsets = (
        (None, {"fields": ("email", "phone_number", "full_name", "password1", "password2")}),
    )

    fieldsets = (
        (None, {"fields": ("email", "phone_number", "full_name", "password")}),
        ("permissions", {"fields": ("is_active" ,"is_admin", "last_login")}),
    )

    search_fields = ("email", "full_name")
    ordering = ("full_name",)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
