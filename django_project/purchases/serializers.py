from rest_framework import serializers

from purchases.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    user_display = serializers.SerializerMethodField()
    book_display = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = ('user', 'user_display', 'book', 'book_display', 'purchase_date')
        read_only_fields = ('user_display', 'book_display', 'purchase_date')
