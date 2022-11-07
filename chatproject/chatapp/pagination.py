from rest_framework import pagination

class Page(pagination.PageNumberPagination):
    page_size = 1


class Pages(pagination.PageNumberPagination):
    page_size = 10