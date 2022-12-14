# Generated by Django 4.1.2 on 2022-11-03 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0017_rename_comments_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="auctions.auctionlisting",
            ),
        ),
    ]
