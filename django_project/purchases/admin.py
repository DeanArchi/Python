from django.contrib import admin

from purchases.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_id', 'get_book_id', 'purchase_date')

    def get_user_id(self, obj):
        if obj.user:
            return f'{obj.user.last_name} {obj.user.first_name}'
        else:
            return None

    get_user_id.short_description = 'user'

    def get_book_id(self, obj):
        if obj.book:
            return obj.book.title
        else:
            return None

    get_book_id.short_description = 'book'
