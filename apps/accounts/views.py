from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from forms import SignUpForm
import account.views

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

User = get_user_model()

class SignUpView(account.views.SignupView):
    form_class = SignUpForm

    def create_user(self, form, commit=True, **kwargs):
        user = super(SignUpView, self).create_user(form=form, commit=False,  **kwargs)
        user.first_name = form.cleaned_data.get("first_name")
        user.last_name = form.cleaned_data.get("last_name")
        if commit:
            user.save()
        return user

class ConfirmEmailView(account.views.ConfirmEmailView):

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm()
        self.after_confirmation(confirmation)
        return super(ConfirmEmailView, self).get(args, kwargs)

    def after_confirmation(self, confirmation):
        user = confirmation.email_address.user
        user.is_active = True
        user.save()

class HomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['all_friends'] = Friend.objects.friends(self.request.user)
        context['user']= self.request.user.username
        return context
