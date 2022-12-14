# Generated by Django 3.1.7 on 2021-06-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20210603_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
