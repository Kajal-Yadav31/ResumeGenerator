# Generated by Django 4.2.1 on 2023-10-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfApp', '0003_alter_profile_specific_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
