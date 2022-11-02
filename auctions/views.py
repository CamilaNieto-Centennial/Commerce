from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, AuctionListing, Category


# Active Listings Page
def index(request):
    return render(request, "auctions/index.html", {
        "auctions": AuctionListing.objects.filter(isActive=True),
        "categories": Category.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# Create a new Listing Page
def createListing (request):
    # GET request method
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            "categories": Category.objects.all()
        })

    # POST request method
    else:
        # Get data from form
        titleField = request.POST["title"]
        descriptionField = request.POST["description"]
        photoField = request.POST["photo"]
        priceField = request.POST["price"]
        categoryField = request.POST["category"] # *

        # Check who is the user
        user = request.user

        # Get info about that specific category *
        categoryInfo = Category.objects.get(categoryTitle=categoryField)

        # Add data to the database
        createdListing = AuctionListing.objects.create(author=user, title=titleField, description=descriptionField, photo=photoField, price=float(priceField), category=categoryInfo)

        # Save data to the database
        createdListing.save()

        return HttpResponseRedirect(reverse("index"))

# Specific Listing Page
def listingPage(request, id):
    listingPage = AuctionListing.objects.get(pk=id)

    # Check who is the user
    user = request.user

    # Check if user makes part of the 'watchlist' row
    isWatchList = user in listingPage.watchlist.all()

    return render(request, "auctions/listing.html", {
        "listingPage": listingPage,
        "isWatchList": isWatchList
    })


# Remove Watchlist (from Listing Page)
def removeWatchlist(request, id):
    auctionListing = AuctionListing.objects.get(pk=id)

    # Check who is the user
    user = request.user

    # Add data to the database (into watchlist row)
    auctionListing.watchlist.remove(user)

    return HttpResponseRedirect(reverse("listingPage", args=(id, )))


# Add Watchlist (from Listing Page)
def addWatchlist(request, id):
    auctionListing = AuctionListing.objects.get(pk=id)

    # Check who is the user
    user = request.user

    # Add data to the database (into watchlist row)
    auctionListing.watchlist.add(user)
    
    return HttpResponseRedirect(reverse("listingPage", args=(id, )))


# Watchlist Page
def watchlist(request):
    # Check who is the user
    user = request.user

    # Get listings added to 'watchlist' row for that specific user
    auctionListings = user.watchlist.all()

    return render(request, "auctions/watchlist.html", {
        "auctions": auctionListings
    })


# Category Feature (Inside of Index Page)
def categorySearch(request):
    # POST request method
    if request.method == "POST":
        chosenCategory = request.POST["category"]
        categoryInfo = Category.objects.get(categoryTitle=chosenCategory)
        
        return render(request, "auctions/index.html", {
            "auctions": AuctionListing.objects.filter(isActive=True, category=categoryInfo),
            "categories": Category.objects.all()
        })
