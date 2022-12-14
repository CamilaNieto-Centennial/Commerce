# Generated by Django 4.1.2 on 2022-11-02 15:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_auctionlisting_iswatchlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="watchlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
