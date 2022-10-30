from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

    def __str__(self):
        return f"STAFF({self.is_staff}): {self.username}" #joined at {self.date_joined}"

# Category Listings Model
class Category(models.Model):
    categoryTitle = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.categoryTitle}" #joined at {self.date_joined}"


# Auction Listings Model
class AuctionListing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600)
    price = models.IntegerField()
    photo = models.URLField(max_length=500)
    isActive = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="category")
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author}"