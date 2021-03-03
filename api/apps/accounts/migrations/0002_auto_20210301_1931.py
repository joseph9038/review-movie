# Generated by Django 3.1.7 on 2021-03-01 19:31

import apps.accounts.helpers
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default=None, null=True, upload_to=apps.accounts.helpers.upload_to_user_avatar_directory),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, choices=[(None, 'Select your role'), ('Student', 'Student'), ('PhD Student', 'PhD Student'), ('Assistant', 'Assistant'), ('Researcher', 'Researcher'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor'), ('Head of Department', 'Head of Department'), ('Head of Faculty', 'Head of Faculty'), ('Head of Laboratory', 'Head of Laboratory'), ('Vice Rector', 'Vice Rector'), ('Rector', 'Rector'), ('Software Developer', 'Software Developer'), ('Engineer', 'Engineer'), ('Technician', 'Technician'), ('Economist', 'Economist'), ('Lawyer', 'Lawyer'), ('Instructor', 'Instructor'), ('Consultant', 'Consultant'), ('Manager', 'Manager'), ('Administrator', 'Administrator'), ('Analyst', 'Analyst'), ('Journalist', 'Journalist'), ('Writer', 'Writer'), ('Editor', 'Editor'), ('Librarian', 'Librarian'), ('Vice Director', 'Vice Director'), ('Chief Executive Officer', 'Chief Executive Officer'), ('Retired', 'Retired'), ('Other', 'Other')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
