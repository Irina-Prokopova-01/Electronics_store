from django.urls import include, path
from rest_framework.routers import SimpleRouter

from supplier.views import (ContactsViewSet, FactoryViewSet, IndividualViewSet,
                            ProductsViewSet, RetailViewSet)

from .apps import SupplierConfig

app_name = SupplierConfig.name

router = SimpleRouter()
router.register(r"factory", FactoryViewSet)
router.register(r"retail", RetailViewSet)
router.register(r"individual", IndividualViewSet)
router.register(r"products", ProductsViewSet)
router.register(r"contacts", ContactsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
