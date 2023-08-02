from rest_framework import serializers

from purchases.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    book_title = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_book_title(self, obj):
        return obj.book.title

    class Meta:
        model = Purchase
        fields = ('user', 'username', 'book', 'book_title', 'purchase_date')
        read_only_fields = ('username', 'book_title', 'purchase_date')
