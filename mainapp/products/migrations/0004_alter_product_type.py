# Generated by Django 4.2.3 on 2023-07-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('beverages', 'beverages'), ('appetizers', 'appetizers'), ('deserts', 'deserts')], max_length=60),
        ),
    ]
