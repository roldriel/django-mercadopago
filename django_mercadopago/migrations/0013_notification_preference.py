# Generated by Django 1.11.2 on 2017-07-01 14:27
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("mp", "0012_untranslated_migrations"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="preference",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications",
                to="mp.Preference",
                verbose_name="preference",
            ),
        ),
    ]
