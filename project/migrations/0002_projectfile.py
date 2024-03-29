# Generated by Django 4.2.5 on 2024-02-06 07:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=225)),
                ("attachment", models.FileField(upload_to="projectfiles")),
            ],
        ),
    ]
