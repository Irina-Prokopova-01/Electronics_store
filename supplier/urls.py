from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .apps import SupplierConfig
from supplier.views import FactoryViewSet, RetailViewSet, IndividualViewSet, ProductsViewSet, ContactsViewSet

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