# Generated by Django 3.1 on 2020-08-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200822_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to='products/media'),
        ),
    ]
