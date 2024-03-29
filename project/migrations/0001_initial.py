# Generated by Django 4.2.5 on 2024-01-21 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("description", models.TextField(blank=True, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
