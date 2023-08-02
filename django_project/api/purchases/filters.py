import django_filters

from purchases.models import Purchase


class PurchaseFilter(django_filters.FilterSet):
    purchase_date = django_filters.DateFromToRangeFilter(field_name='purchase_date')

    class Meta:
        model = Purchase
        fields = {
            'purchase_date': ['exact'],
        }
