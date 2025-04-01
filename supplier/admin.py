from django.contrib import admin
from django.http import HttpResponse
from supplier.models import Factory, Individual_entrepreneur, Retail_chain, Contacts, Products


class CityFilter(admin.SimpleListFilter):
    title = "Город"
    parameter_name = "city"

    def lookups(self, request, model_admin):
        cities = Contacts.objects.values_list("city", flat=True).distinct()
        return [(city, city) for city in cities if city]  # Возвращаем уникальные города для фильтрации

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contacts__city=self.value())
        return queryset



@admin.action(description="Списание задолженности перед поставщиком.")
def delete_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)
    return HttpResponse("Задолженность перед поставщиком списана.")


@admin.display(description="Поставщик")
def get_provider(self, obj):
    if obj.provider_factory:
        return obj.provider_factory.name
    elif obj.provider_retail_chain:
        return obj.provider_retail_chain.name
    return 'Нет поставщика'


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "debt")
    list_filter = ("name", "created_at", CityFilter)
    search_fields = ("name",)
    actions = [delete_debt]


@admin.register(Retail_chain)
class RetailAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "debt", "get_provider")
    list_filter = (CityFilter,)
    search_fields = ("name",)
    actions = [delete_debt]

    @admin.display(description="Поставщик")
    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        return 'Нет поставщика'


@admin.register(Individual_entrepreneur)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ("name", "contacts", "created_at", "debt", "get_provider")
    list_filter = ("name", CityFilter)
    search_fields = ("name",)
    actions = [delete_debt]

    @admin.display(description="Поставщик")
    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        elif obj.provider_retail_chain:
            return obj.provider_retail_chain.name
        return 'Нет поставщика'


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "email", "country", "city")
    list_filter = ("country", "city")
    search_fields = ("name",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "model", "product_launch_date")
    list_filter = ("title",)
