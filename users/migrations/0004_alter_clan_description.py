# Generated by Django 4.2.13 on 2024-07-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_clan_emblem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clan",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
