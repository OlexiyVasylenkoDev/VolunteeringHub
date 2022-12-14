from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class UserTypeChoices(models.TextChoices):
        SINGLE_VOLUNTEER = "Single Volunteer", _("Single Volunteer")
        VOLUNTEERS_ORGANISATION = "Volunteers Organisation", _("Volunteers Organisation")
        CIVIL_PERSON = "Civil Person", _("Civil Person")
        MILITARY_PERSON = "Military Person", _("Military Person")

    type = models.CharField(
        max_length=23,
        choices=UserTypeChoices.choices,
    )
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        unique=True,
        db_index=True,
        editable=False,
    )
    email = models.EmailField(
        _("email address"),
        null=True,
        blank=True,
    )
    phone = PhoneNumberField(
        _("phone"),
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    def __str__(self):
        if self.email:
            return str(self.email)
        else:
            return str(self.phone)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(to="accounts.CustomUser", on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to="profile/", blank=True, null=True, default="profile/profile_default.png")
    name = models.CharField(_("name"), max_length=150, blank=True, null=True, default=None)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True, default=None)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True, default=None)
    city = models.CharField(_("city"), max_length=150, blank=True, null=True, default=None)
    unit = models.CharField(_("unit"), max_length=250, blank=True, null=True, default=None)

    def __str__(self):
        if self.user.email:
            return str(self.user.email)
        else:
            return str(self.user.phone)
