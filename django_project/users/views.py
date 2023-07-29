from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms

from users.models import User


# def users_json(request):
#     users = User.objects.all()
#     data = [{'id': user.id,
#              'username': user.username,
#              'first_name': user.first_name,
#              'last_name': user.last_name}
#             for user in users]
#     return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = ('username', 'password', 'first_name', 'last_name', 'age')
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'age', )
        widgets = {
            'password': forms.PasswordInput()
        }


class UserCreateView(CreateView):
    model = User
    template_name = 'users/user_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('users:user-list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_update.html'
    fields = ('username', 'first_name', 'last_name', 'age')

    def get_success_url(self):
        return reverse_lazy('users:user-detail', kwargs={'pk': self.object.pk})


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('users:user-list')
