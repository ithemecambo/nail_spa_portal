from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.forms import *
from account.models import *


class AccountAdmin(UserAdmin):
    add_form = AccountCreateForm
    form = AccountUpdateForm
    model = Account

    list_display = [
        'id',
        'username',
        'get_full_name',
        'email',
        'admin',
        'is_staff',
        'active',
    ]
    list_display_links = [
        'id',
        'username',
        'get_full_name',
        'email',
    ]
    list_filter = [
        'created_at',
        'is_active',
        'is_admin',
        'is_staff'
    ]
    search_fields = [
        'first_name',
        'last_name',
        'phone',
        'fax',
        'email'
    ]

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email',
                       'password1', 'password2', 'is_admin', 'is_staff', 'is_active')}
         ),
    )
    ordering = [
        'id',
        'first_name'
    ]
    ordering = ['-id']
    list_per_page = 12


class StaffAdmin(admin.ModelAdmin):
    list_display = ['profile', 'name', 'nickname', 'fax', 'ssn']
    list_display_links = ['profile', 'name', 'nickname', 'fax', 'ssn']
    ordering = ['nickname',]
    list_per_page = 12


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'name', 'phone', 'city', 'state', 'zipcode']
    list_display_links = ['profile', 'name', 'phone', 'city']
    list_per_page = 12


admin.site.register(Account, AccountAdmin)
admin.site.register(StaffProfile, StaffAdmin)
admin.site.register(Profile, ProfileAdmin)
