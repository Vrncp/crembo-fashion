# Generated by Django 4.1.7 on 2023-03-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0028_remove_product_detalle_alter_product_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomercancia',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
