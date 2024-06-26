# Generated by Django 4.2.9 on 2024-04-21 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Area",
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
                ("name", models.CharField(max_length=30)),
                ("capacity", models.IntegerField(blank=True, null=True)),
                (
                    "areaType",
                    models.CharField(
                        choices=[
                            ("T", "Tente"),
                            ("C", "Caravan"),
                            ("H", "Room"),
                            ("N", "Notarea"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Areas", "ordering": ("name",),},
        ),
        migrations.CreateModel(
            name="Address",
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
                ("name", models.CharField(max_length=30)),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="area.area",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Addresses", "ordering": ("name",),},
        ),
    ]
