# Generated by Django 3.1 on 2020-08-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200826_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
