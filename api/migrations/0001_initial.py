# Generated by Django 4.1.5 on 2023-01-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="company",
            fields=[
                ("company_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=55)),
                ("location", models.CharField(max_length=255)),
                ("about", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("IT", "IT"),
                            ("Non IT", "Non IT"),
                            ("Mobile Phones", "Mobile Phones"),
                        ],
                        max_length=100,
                    ),
                ),
                ("added_date", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
