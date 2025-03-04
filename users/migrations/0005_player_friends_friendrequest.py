# Generated by Django 4.2.13 on 2024-07-13 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_clan_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="friends",
            field=models.ManyToManyField(blank=True, to="users.player"),
        ),
        migrations.CreateModel(
            name="FriendRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_request",
                        to="users.player",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_request",
                        to="users.player",
                    ),
                ),
            ],
        ),
    ]
