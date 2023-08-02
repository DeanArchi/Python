from rest_framework.pagination import PageNumberPagination


class UserCustomPagination(PageNumberPagination):
    page_size = 10
