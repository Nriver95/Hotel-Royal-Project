# Generated by Django 4.2.3 on 2023-08-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('deserts', 'deserts'), ('beverages', 'beverages'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
