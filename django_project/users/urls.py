from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('create/', views.UserCreateView.as_view(), name='user-create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
]
