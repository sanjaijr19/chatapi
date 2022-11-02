from rest_framework import pagination

class Page(pagination.PageNumberPagination):
    page_size = 1