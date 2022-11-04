from django.contrib import admin

from .models import User, AuctionListing, Category, Comment, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(AuctionListing)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Bid)