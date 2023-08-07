from rest_framework.viewsets import ModelViewSet

from api.purchases.filters import PurchaseFilter
from api.purchases.serializers import PurchaseSerializer
from purchases.models import Purchase


class PurchaseModelViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_class = PurchaseFilter
    search_fields = ('username', 'book_title')
    ordering_fields = ('purchase_date',)
