from decimal import Decimal

from django.db import models

LEVEL = [
    (1, "1"),
    (2, "2"),
]

LEVEL_factory = [
    (0, "0"),
]


class Contacts(models.Model):
    """Модель контактов"""
    title = models.CharField(max_length=255, verbose_name="Укажите название компании")
    email = models.EmailField(help_text="Укажите почту компании")
    country = models.CharField(max_length=255, verbose_name="Укажите страну")
    city = models.CharField(max_length=255, verbose_name="Укажите город")
    street = models.CharField(max_length=255, verbose_name="Укажите улицу")
    house_number = models.PositiveIntegerField(verbose_name="Укажите номер дома")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def city_filters(self):
        return self.city_filters()

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("city",)

    def __str__(self):
        return f"{self.title}, {self.email}, {self.country}"


class Products(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Название модели")
    product_launch_date = models.DateField(verbose_name="Дата выхода продукта на рынок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("product_launch_date",)

    def __str__(self):
        return f"{self.title}, {self.model}"


class Factory(models.Model):
    """Модель завода"""
    name = models.CharField(max_length=255, verbose_name="Укажите название компании")
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name="factory_contacts", verbose_name="Контакты")
    products = models.ManyToManyField(Products, verbose_name="Продукты")
    # provider_factory = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="factory_factory_providers", verbose_name="Поставщик завод")
    level = models.PositiveIntegerField(verbose_name="Уровень в иерархии", choices=LEVEL_factory, default=0)
    debt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal('0.00'), verbose_name="Задолжность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name}, {self.contacts}"



class Retail_chain(models.Model):
    """Модель розничной сети"""
    name = models.CharField(max_length=255, verbose_name="Укажите название компании")
    contacts = models.OneToOneField(Contacts, related_name="retail_chain_contacts", on_delete=models.CASCADE, verbose_name="Контакты")
    products = models.ManyToManyField(Products, verbose_name="Продукты")
    # provider_retail_chain = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="retail_chain_retail_chain_providers", verbose_name="Поставщик сеть")
    provider_factory = models.ForeignKey(Factory, on_delete=models.SET_NULL, blank=True, null=True, related_name="Поставщик", verbose_name="Поставщик завод")
    level = models.PositiveIntegerField(verbose_name="Уровень в иерархии", choices=LEVEL, default=1)
    debt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal('0.00'), verbose_name="Задолжность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name}, {self.contacts}"

    def get_provider(self):
        """Идентификация поставщика"""
        if self.provider_factory:
            return self.provider_factory.name
        return 'Нет поставщика'

    # def get_level(self):
    #     """Присвоение уровня в иерархии"""
    #     level = 0
    #     factory_level = self.provider_factory
    #     while factory_level:
    #         level += 1
    #         factory_level = factory_level.provider_factory
    #     self.level = level


class Individual_entrepreneur(models.Model):
    """Модель ИП"""
    name = models.CharField(max_length=255, verbose_name="Укажите название компании")
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name="individual_entrepreneur_contacts", verbose_name="Контакты")
    products = models.ManyToManyField(Products, verbose_name="Продукты")
    level = models.PositiveIntegerField(verbose_name="Уровень в иерархии", choices=LEVEL, default=2)
    provider_factory = models.ForeignKey(Factory, on_delete=models.SET_NULL, blank=True, null=True, related_name="individual_entrepreneur_factory_providers", verbose_name="Поставщик завод")
    provider_retail_chain = models.ForeignKey(Retail_chain, on_delete=models.SET_NULL, blank=True, null=True, related_name="individual_entrepreneur_retail_chain_providers", verbose_name="Поставщик ритейлер")
    # provider_individual_entrepreneur = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="individual_entrepreneur_Individual_entrepreneur_providers", verbose_name="Поставщик ИП")
    debt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal('0.00'), verbose_name="Задолжность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Предприниматель"
        verbose_name_plural = "Предприниматели"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name}, {self.contacts}"

    def get_provider(self):
        """Идентификация поставщика"""
        if self.provider_factory:
            return self.provider_factory.name
        elif self.provider_retail_chain:
            return self.provider_retail_chain.name
        return 'Нет поставщика'

    # def get_level(self):
    #     """Присвоение уровня в иерархии"""
    #     level = 0
    #     if self.provider_factory:
    #         level += 1
    #         return level
    #     elif self.provider_retail_chain:
    #         level +=2
    #         return level
    #     return "Уровень поставщика не определен"

