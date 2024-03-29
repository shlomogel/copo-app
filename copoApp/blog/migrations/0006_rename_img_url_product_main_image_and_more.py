# Generated by Django 5.0.2 on 2024-03-03 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_product_due_date_productimage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="img_url",
            new_name="main_image",
        ),
        migrations.AlterField(
            model_name="product",
            name="due_date",
            field=models.DateField(
                default=datetime.datetime(2024, 3, 17, 19, 51, 6, 132724)
            ),
        ),
    ]
