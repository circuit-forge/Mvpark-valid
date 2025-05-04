from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


def landing_page(request):
    return render(request, 'users/landing_page.html')

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Waitlist  # Import your model if you have one

def join_waitlist(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Check if email already exists
        if Waitlist.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered!")
        else:
            Waitlist.objects.create(email=email)
            messages.success(request, "Thanks for joining the waitlist!")

        return redirect('/')
        
    return redirect('/')

def show_waitlist(request):
    emails = [entry.email for entry in Waitlist.objects.all()]
    return HttpResponse("<br>".join(emails))


def count_signups(request):
    count = Waitlist.objects.count()
    return HttpResponse(f"<h1>Total signups: {count}</h1>")



