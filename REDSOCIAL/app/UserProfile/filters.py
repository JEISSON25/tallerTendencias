# app/UserProfile/filters.py

import django_filters
from .models import UserProfile

class UserProfileFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'bio': ['exact'],

        }
        filter_overrides = {

        }
