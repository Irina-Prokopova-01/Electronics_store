from rest_framework import serializers
from supplier.validators import change_debt

from supplier.models import Contacts, Factory, Products, Individual_entrepreneur, Retail_chain


class ContactsSerializer(serializers.ModelSerializer):
    """
    Сериализатор отзыва
    """

    class Meta:
        model = Contacts
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    """
    Сериализатор отзыва
    """

    class Meta:
        model = Products
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели завода"""
    contacts = ContactsSerializer()

    def create(self, validation_data):
        contacts = Contacts.objects.create(**validation_data.pop("contacts"))
        factory = Factory.objects.create(contacts=contacts, **validation_data)
        return factory

    class Meta:
        model = Factory
        fields = "__all__"

    debt = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        required=False,
        allow_null=True,
        validators=[change_debt]
    )


class IndividualSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ИП"""
    contacts = ContactsSerializer()

    def create(self, validation_data):
        contacts = Contacts.objects.create(**validation_data.pop("contacts"))
        individual_entrepreneur = Individual_entrepreneur.objects.create(contacts=contacts, **validation_data)
        return individual_entrepreneur

    class Meta:
        model = Individual_entrepreneur
        fields = "__all__"

    debt = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        required=False,
        allow_null=True,
        validators=[change_debt]
    )


class RetailSerializer(serializers.ModelSerializer):
    """Сериализатор для модели сети"""
    contacts = ContactsSerializer()

    def create(self, validation_data):
        contacts = Contacts.objects.create(**validation_data.pop("contacts"))
        retail_chain = Retail_chain.objects.create(contacts=contacts, **validation_data)
        return retail_chain

    class Meta:
        model = Retail_chain
        fields = "__all__"

    debt = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        required=False,
        allow_null=True,
        validators=[change_debt]
    )

