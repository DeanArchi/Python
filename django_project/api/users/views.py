from rest_framework.viewsets import ModelViewSet

from api.users.filters import UserFilter
from api.users.pagination import UserCustomPagination
from api.users.serializers import UserSerializer
from users.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserCustomPagination
    filterset_class = UserFilter
    search_fields = ('first_name', 'last_name')
    ordering_fields = ('age',)
