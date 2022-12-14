# Generated by Django 4.1.4 on 2022-12-07 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("New_API", "0002_alter_address_pin_alter_person_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="person",
                to="New_API.address",
            ),
        ),
    ]
