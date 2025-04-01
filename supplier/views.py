from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from supplier.models import Products, Contacts, Factory, Individual_entrepreneur, Retail_chain
from supplier.paginators import SupplierPagination
from users.permissions import IsActiveUser
from supplier.serializers import (
    ProductsSerializer,
    ContactsSerializer,
    FactorySerializer,
    IndividualSerializer,
    RetailSerializer,
)


class ProductsViewSet(viewsets.ModelViewSet):
    """CRUD для работы с продуктами"""
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = SupplierPagination
    permission_classes = [AllowAny]


class ContactsViewSet(viewsets.ModelViewSet):
    """CRUD для работы с контактами"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    pagination_class = SupplierPagination
    permission_classes = [AllowAny]


class FactoryViewSet(viewsets.ModelViewSet):
    """CRUD для работы с поставщиками"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    pagination_class = SupplierPagination
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["contacts__country"]


class IndividualViewSet(viewsets.ModelViewSet):
    """CRUD для работы с поставщиками"""
    queryset = Individual_entrepreneur.objects.all()
    serializer_class = IndividualSerializer
    pagination_class = SupplierPagination
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["contacts__country"]


class RetailViewSet(viewsets.ModelViewSet):
    """CRUD для работы с поставщиками"""
    queryset = Retail_chain.objects.all()
    serializer_class = RetailSerializer
    pagination_class = SupplierPagination
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["contacts__country"]