# Generated by Django 3.1 on 2020-08-26 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_remove_article_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]