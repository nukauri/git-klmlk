# Generated by Django 4.2.9 on 2024-07-05 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("area", "0001_initial"),
        ("account", "0002_alter_account_documenttype"),
    ]

    operations = [
        migrations.CreateModel(
            name="Credit",
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
                        related_name="credits",
                        to="area.area",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="credits",
                        to="account.supplier",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Credits", "ordering": ("customer",),},
        ),
    ]
