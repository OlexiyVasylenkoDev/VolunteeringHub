from django.contrib.auth import get_user_model

from volunteering.models import Category, Opportunity, Need, Accounting


def sample_user(**params):
    defaults = {
        "type": "Single Volunteer",
        "username": "Username",
        "email": "email@email.com",
        "phone": "+380630000000",
        "is_staff": True,
        "is_active": True,
    }
    defaults.update(**params)
    return get_user_model().objects.create(**defaults)


def sample_category(**params):
    return Category.objects.create(**params)


def sample_opportunity(**params):
    defaults = {"description": "Description"}
    defaults.update(params)
    return Opportunity.objects.create(**defaults)


def sample_need(**params):
    defaults = {"description": "Description"}
    defaults.update(params)
    return Need.objects.create(**defaults)


def sample_accounting(**params):
    return Accounting.objects.create(**params)
