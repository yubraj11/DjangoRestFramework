# Generated by Django 4.1.5 on 2023-02-09 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_alter_user_phone"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="user",
            table="account_user",
        ),
    ]
