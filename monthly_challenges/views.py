from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january":"Eat no meat for the entire month",
    "february" : "walk for at least 20 minutes every day",
    "march":"save about one million naira everyday",
    "april" : "Start saving at least one million naira each day.",
    "may" : "Aim to set aside one million naira daily.",
    "june" : "Try to save about one million naira every day.",
    "july" : "Focus on saving one million naira each day.",
    "august" : "Commit to saving one million naira on a daily basis.",
    "september" : "Work towards saving one million naira every single day.",
    "october" : "Make it a goal to save one million naira daily.",
    "november" : "Set a target of saving one million naira each day.",
    "december" : None
    
}

def index(request):
    
    months = monthly_challenges.keys()
    
    context = {
        "months" : months,
    }
    
    return render(request, "index.html", context)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")
        
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = {
            "challenge_text" : challenge_text,
            "month" : month,
        }
        return render(request, "monthly_challenge.html", context)
    except:
       raise Http404()
    