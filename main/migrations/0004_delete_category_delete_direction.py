# Generated by Django 4.1.7 on 2023-02-20 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_category_name_category_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Direction',
        ),
    ]
