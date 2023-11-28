from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.forms import *
from account.models import Account


class AccountAdmin(UserAdmin):
    add_form = AccountCreateForm
    form = AccountUpdateForm
    model = Account

    list_display = [
        'profile',
        'get_full_name',
        'phone',
        'fax',
        'email',
        'admin',
        'staff',
        'active',
    ]
    list_display_links = [
        'profile',
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
        (None, {'fields': ('first_name', 'last_name', 'nickname', 'gender', 'phone', 'fax', 'ssn', 'address', 'photo_url')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'nickname', 'gender', 'phone', 'fax', 'ssn', 'address', 'photo_url', 'username', 'email',
                       'password1', 'password2', 'is_admin', 'is_staff', 'is_active')}
         ),
    )
    ordering = [
        'id',
        'first_name'
    ]


admin.site.register(Account, AccountAdmin)
