# Generated by Django 4.2.3 on 2023-07-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('deserts', 'deserts'), ('beverages', 'beverages'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
