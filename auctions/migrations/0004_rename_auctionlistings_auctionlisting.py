# Generated by Django 4.1.2 on 2022-10-29 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_user_datecreated_alter_auctionlistings_datecreated"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="auctionListings",
            new_name="AuctionListing",
        ),
    ]