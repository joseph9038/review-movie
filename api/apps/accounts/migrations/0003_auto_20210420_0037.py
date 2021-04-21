# Generated by Django 3.1.7 on 2021-04-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210409_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, choices=[(None, 'Select your role'), ('Administrator', 'Administrator'), ('Artist', 'Artist'), ('College', 'College'), ('Customer Service', 'Customer Service'), ('Doctor', 'Doctor'), ('Educator', 'Educator'), ('Executive', 'Executive'), ('Farmer', 'Farmer'), ('Homemaker', 'Homemaker'), ('Lawyer', 'Lawyer'), ('Other', 'Other'), ('Programmer', 'Programmer'), ('Retired', 'Retired'), ('Sales', 'Sales'), ('Scientist', 'Scientist'), ('Self-employed', 'Self-employed'), ('Student', 'Student'), ('Technician', 'Technician'), ('Tradesman', 'Tradesman'), ('Unemployed', 'Unemployed'), ('Writer', 'Writer')], default=None, max_length=30, null=True),
        ),
    ]
