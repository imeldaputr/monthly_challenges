from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse # Create URLs dynamically

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Practice coding for at least 30 minutes every day!",
    "may": "Read a book for at least 20 minutes every day!",
    "june": "Meditate for at least 10 minutes every day!",
    "july": "Drink at least 2 liters of water every day!",
    "august": "Write a journal entry every day!",
    "september": "Try a new hobby for at least 30 minutes every day!",
    "october": "Spend at least 30 minutes outdoors every day!",
    "november": "Practice gratitude by writing down 3 things you're thankful for every day!",
    "december": None
}

# Create your views here.
# A function or a class that takes a request and returns a response


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path) # 302: redirect response


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        }) 
    except:
        raise Http404()