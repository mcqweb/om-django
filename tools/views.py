from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import UserToolPermission, TwoUp, Event
from collections import defaultdict

def landing(request):
    tools = []
    is_admin = False
    if request.user.is_authenticated:
        tools = UserToolPermission.objects.filter(user=request.user).select_related('tool')
        is_admin = request.user.groups.filter(name='admin').exists() or request.user.is_superuser
    return render(request, "landing.html", {"tools": tools, "is_admin": is_admin})

@login_required
def two_ups(request):
    data = TwoUp.objects.all()
    # Build a mapping of event_id to event object
    events = {e.id: e for e in Event.objects.filter(id__in=[d.event_id for d in data])}
    return render(request, "tools/two_ups.html", {"data": data, "events": events})

@login_required
def racing_matcher(request):
    return render(request, "tools/racing_matcher.html")

@login_required
def willhillbb(request):
    return render(request, "tools/willhillbb.html")
