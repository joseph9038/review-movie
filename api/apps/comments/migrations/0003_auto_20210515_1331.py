# Generated by Django 3.1.7 on 2021-05-15 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210513_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
    ]
