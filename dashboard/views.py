from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from concussiontest.models import Athlete

# Create your views here.

@login_required
def dashboard(request):
    athletes = Athlete.objects.all()
    print(athletes)
    return render(request, 'dashboard/dashboard.html', {'section': 'dashboard',
                                                        'athletes': athletes})