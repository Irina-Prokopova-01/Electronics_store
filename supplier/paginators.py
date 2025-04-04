from rest_framework.pagination import PageNumberPagination


class SupplierPagination(PageNumberPagination):
    page_size = 6  # Кол-во элементов на странице
    page_size_query_param = (
        "page_size"  # Параметр запроса для указания количества элементов на странице
    )
    max_page_size = 6  # Максимальное кол-во элементов на странице
