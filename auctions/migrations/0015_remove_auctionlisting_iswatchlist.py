# Generated by Django 4.1.2 on 2022-11-02 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0014_auctionlisting_watchlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="isWatchList",
        ),
    ]
