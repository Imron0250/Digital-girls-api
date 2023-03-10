# Generated by Django 4.1.7 on 2023-02-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_category_delete_direction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='map',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='numer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
