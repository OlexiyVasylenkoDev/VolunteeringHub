# Generated by Django 4.1.1 on 2022-11-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_customuser_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customprofile",
            name="photo",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="profile/"
            ),
        ),
    ]
