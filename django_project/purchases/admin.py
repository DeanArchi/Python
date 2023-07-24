from django.contrib import admin

from purchases.models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'purchase_date')

    def user(self, obj):
        if obj.user:
            return f'{obj.user.last_name} {obj.user.first_name}'
        else:
            return None

    user.short_description = 'user'

    def book(self, obj):
        if obj.book:
            return obj.book.title
        else:
            return None

    book.short_description = 'book'
