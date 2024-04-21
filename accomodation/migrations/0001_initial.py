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
            name="Accomodation",
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
                ("startDate", models.DateField()),
                ("endDate", models.DateField(blank=True, null=True)),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("tlfNo", models.CharField(blank=True, max_length=30, null=True)),
                ("plaka", models.CharField(blank=True, max_length=30, null=True)),
                ("status", models.BooleanField(blank=True, null=True)),
                ("is_paid", models.BooleanField(blank=True, null=True)),
                ("is_closed", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accomodations",
                        to="area.address",
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accomodations",
                        to="area.area",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accomodations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Accomodations", "ordering": ("name",),},
        ),
    ]
