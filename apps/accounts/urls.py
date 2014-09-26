from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import SignUpView, ConfirmEmailView, HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^account/signup/$', SignUpView.as_view(), name="account_signup"),
    url(r'^account/confirm_email/(?P<key>\w+)/$', ConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r'^account/', include('account.urls')),
)