# Generated by Django 3.1 on 2020-08-22 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to='images/'),
        ),
    ]
