from django import forms
from django.utils.translation import ugettext_lazy as _
import account.forms


class SignUpForm(account.forms.SignupForm):
    first_name = forms.CharField(max_length=30, label=_('First Name'))
    last_name = forms.CharField(max_length=30, label=_('Last Name'))
