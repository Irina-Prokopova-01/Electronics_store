from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from supplier.models import (Contacts, Factory, Individual_entrepreneur,
                             Products, Retail_chain)
from users.models import User


class ElectronicsNetworkCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com", password="12345")
        # Создаем контакты
        self.contacts = Contacts.objects.create(
            title="Завод1",
            email="zavod1@mail.ru",
            country="Россия",
            city="Москва",
            street="Ленина",
            house_number=2,
            created_at="2025-03-31T11:12:20.913265+03:00",
        )

        # Создаем продукты
        self.products = Products.objects.create(
            title="Продукт 1",
            model="1",
            product_launch_date="2024-05-27",
            created_at="2025-03-31T11:12:20.913265+03:00",
        )

        # Создаем завод
        self.factory = Factory.objects.create(
            name="Завод1",
            contacts=self.contacts,
            level=0,
            debt=25000.00,
            created_at="2025-03-31T11:12:20.913265+03:00",
        )
        self.factory.products.set([self.products])

        # Создаем розничную сеть
        self.retail_chain = Retail_chain.objects.create(
            name="Розница1",
            contacts=self.contacts,
            level=2,
            debt=370000.00,
            created_at="2025-03-31T11:12:20.913265+03:00",
            provider_factory=self.factory,
        )
        self.retail_chain.products.set([self.products])

        # Создаем индивидуального предпринимателя
        self.entrepreneur = Individual_entrepreneur.objects.create(
            name="ИП1",
            contacts=self.contacts,
            level=2,
            debt=39000.00,
            created_at="2025-03-31T11:12:20.913265+03:00",
            provider_factory=self.factory,
            provider_retail_chain=self.retail_chain,
        )
        self.entrepreneur.products.set([self.products])

        self.client.force_authenticate(user=self.user)

    def test_factory_detail(self):
        url = reverse("supplier:factory-detail", args=(self.factory.pk,))
        response = self.client.get(url)
        print(response)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.factory.name)

    def test_retail_chain_detail(self):
        url = reverse("supplier:retail_chain-detail", args=(self.factory.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.retail_chain.name)

    def test_individual_entrepreneur_detail(self):
        url = reverse(
            "supplier:individual_entrepreneur-detail", args=(self.factory.pk,)
        )
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.entrepreneur.name)

    def test_factory_list(self):
        url = reverse("supplier:factory-list")
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_retail_chain_list(self):
        url = reverse("supplier:retail_chain-list")
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_entrepreneur_list(self):
        url = reverse("supplier:individual_entrepreneur-list")
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


# import pytest
# import json
# from rest_framework import status
# from django.urls import reverse
# from supplier.models import Factory, Individual_entrepreneur, Contacts, Products, Retail_chain
# from users.models import User
# from rest_framework.test import APIClient
#
#
# @pytest.fixture
# def api_client():
#     return APIClient()
#
#
# @pytest.fixture
# def create_user(db):
#     return User.objects.create(email="test@yandex.ru", password="12345")
#
# @pytest.fixture
# def create_contacts(db):
#     return Contacts.objects.create(title="ИП Галай", email="galay@yandex.ru", country="Россия", city="Бийск", street="Ленина", house_number=2,)
#
# @pytest.fixture
# def create_products(db):
#     return User.objects.create(title="Пила", model="122", product_launch_date="2020-03-27")
#
#
# @pytest.fixture
# def create_factory(db, create_user):
#     return Factory.objects.create(
#         author=create_user,
#         name="Завод 1",
#         level="2",
#         debt=100
#     )
#
#
# def test_user_create_factory(api_client, create_user):
#     """Проверяем может ли пользователь создать обьявление"""
#     api_client.force_authenticate(user=create_user)
#
#     url = reverse("supplier:factory-list")
#     data = {
#         "author": create_user.id,
#         "contacts": {
#                 "title": "OOO Электроник",
#                 "email": "electronic@yandex.ru",
#                 "country": "Россия",
#                 "city": "Истра",
#                 "street": "Ленина",
#                 "house_number": 5,
#                 "created_at": "2025-03-28T12:48:54.466281+03:00"
#             },
#         "products": 2,
#         "name": "Завод 1",
#         "level": 2,
#         "debt": 100.00
#     }
#
#     response = api_client.post(url, data, format='json')
#     print(response.content)  # Выводим содержимое ответа для отладки
#     assert response.status_code == status.HTTP_201_CREATED
#     assert Factory.objects.count() == 1
#     assert Factory.objects.get().title == "Новый завод"
