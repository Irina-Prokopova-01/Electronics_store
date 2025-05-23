# Generated by Django 5.1.7 on 2025-03-28 09:46

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, verbose_name="Укажите название компании"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Укажите почту компании", max_length=254
                    ),
                ),
                (
                    "country",
                    models.CharField(max_length=255, verbose_name="Укажите страну"),
                ),
                (
                    "city",
                    models.CharField(max_length=255, verbose_name="Укажите город"),
                ),
                (
                    "street",
                    models.CharField(max_length=255, verbose_name="Укажите улицу"),
                ),
                (
                    "house_number",
                    models.PositiveIntegerField(verbose_name="Укажите номер дома"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
                "ordering": ("city",),
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название продукта"),
                ),
                (
                    "model",
                    models.CharField(max_length=255, verbose_name="Название модели"),
                ),
                (
                    "product_launch_date",
                    models.DateField(verbose_name="Дата выхода продукта на рынок"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ("product_launch_date",),
            },
        ),
        migrations.CreateModel(
            name="Factory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Укажите название компании"
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        null=True,
                        verbose_name="Задолжность перед поставщиком",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "contacts",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="factory_contacts",
                        to="supplier.contacts",
                    ),
                ),
                ("products", models.ManyToManyField(to="supplier.products")),
            ],
            options={
                "verbose_name": "Завод",
                "verbose_name_plural": "Заводы",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Retail_chain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Укажите название компании"
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        null=True,
                        verbose_name="Задолжность перед поставщиком",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "contacts",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="retail_chain_contacts",
                        to="supplier.contacts",
                    ),
                ),
                ("products", models.ManyToManyField(to="supplier.products")),
                (
                    "provider_factory",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Поставщик",
                        to="supplier.factory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сеть",
                "verbose_name_plural": "Сети",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Individual_entrepreneur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Укажите название компании"
                    ),
                ),
                (
                    "debt",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=10,
                        null=True,
                        verbose_name="Задолжность перед поставщиком",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "contacts",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="individual_entrepreneur_contacts",
                        to="supplier.contacts",
                    ),
                ),
                (
                    "provider_factory",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="individual_entrepreneur_factory_providers",
                        to="supplier.factory",
                    ),
                ),
                ("products", models.ManyToManyField(to="supplier.products")),
                (
                    "provider_retail_chain",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="individual_entrepreneur_retail_chain_providers",
                        to="supplier.retail_chain",
                    ),
                ),
            ],
            options={
                "verbose_name": "Предприниматель",
                "verbose_name_plural": "Предприниматели",
                "ordering": ("-created_at",),
            },
        ),
    ]
