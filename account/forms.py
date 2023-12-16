from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import Account


class AccountCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'email'
        ]

class AccountUpdateForm(UserChangeForm):
    class Meta:
        model = Account
        fields = [
            'email'
        ]

