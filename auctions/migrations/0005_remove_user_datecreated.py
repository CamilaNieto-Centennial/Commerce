# Generated by Django 4.1.2 on 2022-10-29 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_rename_auctionlistings_auctionlisting"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="dateCreated",
        ),
    ]