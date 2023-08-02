import django_filters

from users.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['exact', 'contains'],
            'last_name': ['exact', 'contains'],
            'age': ['exact', 'gte', 'lte', 'range']
        }
