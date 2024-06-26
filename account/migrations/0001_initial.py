# Generated by Django 4.2.9 on 2024-04-21 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("area", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banka",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "Banka", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="CurrencyUnit",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "CurrencyUnits", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="DocumentGroup",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={"verbose_name_plural": "DocumentGroups", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="DocumentType",
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
                ("name", models.CharField(max_length=255)),
                (
                    "accountType",
                    models.CharField(
                        choices=[("GL", "Gelir"), ("GD", "Gider")], max_length=2
                    ),
                ),
            ],
            options={"verbose_name_plural": "DocumentTypes", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="PayType",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "PayType", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "Projects", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("name", models.CharField(max_length=255)),
                ("isCustomer", models.BooleanField(blank=True, null=True)),
                ("isSupplier", models.BooleanField(blank=True, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("contact", models.CharField(blank=True, max_length=35, null=True)),
                ("phoneNumber", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={"verbose_name_plural": "Suppliers", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="Debit",
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
                ("invoiceDate", models.DateField(blank=True, null=True)),
                ("invoicePrice", models.FloatField(blank=True, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("paymentTerm", models.IntegerField(blank=True, null=True)),
                (
                    "area",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debits",
                        to="area.area",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debits",
                        to="account.supplier",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Debits", "ordering": ("supplier",),},
        ),
        migrations.CreateModel(
            name="Account",
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
                ("documentDate", models.DateField()),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("price", models.FloatField()),
                (
                    "documentImage",
                    models.ImageField(blank=True, null=True, upload_to="item_images"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "area",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="area.area",
                    ),
                ),
                (
                    "banka",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="account.banka",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "currencyUnit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="account.currencyunit",
                    ),
                ),
                (
                    "documentType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="account.documenttype",
                    ),
                ),
                (
                    "payType",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="account.paytype",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts",
                        to="account.supplier",
                    ),
                ),
            ],
        ),
    ]
