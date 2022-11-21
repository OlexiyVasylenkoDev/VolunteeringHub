# Generated by Django 4.1.1 on 2022-11-19 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Accounting",
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
                    "description",
                    models.TextField(blank=True, default=None, null=True, verbose_name="description"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="accounting/",
                        verbose_name="photo",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounting_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Accounting",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=256, verbose_name="name")),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Opportunity",
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
                ("title", models.CharField(max_length=100, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, default=None, null=True, verbose_name="description"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="opportunity/",
                        verbose_name="photo",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=150,
                        null=True,
                        verbose_name="city",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="opportunity_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(related_name="category", to="volunteering.category"),
                ),
            ],
            options={
                "verbose_name_plural": "Opportunities",
            },
        ),
        migrations.CreateModel(
            name="Need",
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
                ("title", models.CharField(max_length=100, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, default=None, null=True, verbose_name="description"),
                ),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="need/", verbose_name="photo"),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=20,
                        null=True,
                        verbose_name="price",
                    ),
                ),
                (
                    "donation",
                    models.URLField(blank=True, null=True, verbose_name="donation"),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        default=None,
                        max_length=150,
                        null=True,
                        verbose_name="city",
                    ),
                ),
                ("is_satisfied", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "accounting",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="needs",
                        to="volunteering.accounting",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="need_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="needs",
                        to="volunteering.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
