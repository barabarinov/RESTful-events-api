# Generated by Django 5.1.4 on 2024-12-15 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0003_event_guests"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="date",
            new_name="datetime",
        ),
    ]
