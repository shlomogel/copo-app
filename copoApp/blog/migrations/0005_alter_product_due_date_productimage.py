# Generated by Django 5.0.2 on 2024-03-03 17:26

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_product_due_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="due_date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 17, 19, 26, 25, 378274)
            ),
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                ("img_url", models.URLField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="blog.product",
                    ),
                ),
            ],
        ),
    ]
