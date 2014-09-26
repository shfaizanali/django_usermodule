from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name=None, last_name=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        #
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name=None, last_name=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, verbose_name=_('First Name'), blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name=_('Last Name'), blank=True, null=True)
    username = models.CharField(max_length=60, unique=True, verbose_name=_('Username'))
    email = models.EmailField(
        verbose_name=_('Email Address'),
        unique=True,
    )

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    profile_avatar = models.ImageField(upload_to='avatars')
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

