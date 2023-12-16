from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.forms import *
from account.models import *


class AccountAdmin(UserAdmin):
    add_form = AccountCreateForm
    form = AccountUpdateForm
    model = Account

    list_display = [
        'username',
        'get_full_name',
        'phone',
        'email',
        'admin',
        'is_staff',
        'active',
    ]
    list_display_links = [
        'username',
        'get_full_name',
        'phone',
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
    list_per_page = 10
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'gender', 'phone')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'gender', 'phone', 'username', 'email',
                       'password1', 'password2', 'is_admin', 'is_staff', 'is_active')}
         ),
    )
    ordering = [
        'id',
        'first_name'
    ]


class StaffAdmin(admin.ModelAdmin):
    list_display = ['profile', 'name', 'nickname', 'fax', 'ssn']


admin.site.register(Account, AccountAdmin)
admin.site.register(StaffProfile, StaffAdmin)
admin.site.register(Profile)
