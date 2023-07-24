import json

from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from purchases.models import Purchase


# def purchases_json(request):
#     purchases = Purchase.objects.select_related('user', 'book').values(
#         'id',
#         'user__first_name',
#         'user__last_name',
#         'book__title',
#         'book__price',
#         'purchase_date'
#     )
#     data = [{"purchase_id": purchase['id'],
#              'first_name': purchase['user__first_name'],
#              'last_name': purchase['user__last_name'],
#              'title': purchase['book__title'],
#              'price': purchase['book__price'],
#              'purchase_date': purchase['purchase_date'].strftime('%Y-%m-%d %H:%M:%S')}
#             for purchase in purchases]
#     return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchases/purchases_list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return Purchase.objects.select_related('user', 'book')


class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchases/purchases_detail.html'
    context_object_name = 'purchase'

    def get_queryset(self):
        return Purchase.objects.select_related('user', 'book')


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['user', 'book']


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = 'purchases/purchase_create.html'
    form_class = PurchaseCreateForm
    success_url = reverse_lazy('purchases:purchase-list')


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'purchases/purchase_delete.html'
    context_object_name = 'purchase'
    success_url = reverse_lazy('purchases:purchase-list')
