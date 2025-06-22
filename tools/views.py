from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import UserToolPermission, TwoUp
from collections import defaultdict
from django.utils import timezone
from tools.utils import generate_supabase_tokens
from django.conf import settings
from .supabase_admin import create_supabase_user
from django.db import transaction
from betting_data.models import Event

def landing(request):
    tools = []
    is_admin = False
    if request.user.is_authenticated:
        tools = UserToolPermission.objects.filter(user=request.user).select_related('tool')
        is_admin = request.user.groups.filter(name='admin').exists() or request.user.is_superuser
    return render(request, "landing.html", {"tools": tools, "is_admin": is_admin})

@login_required
def two_ups(request):
    now = timezone.now()
    # Get all events in the future
    future_events = Event.objects.filter(event_date__gte=now)
    event_ids = [e.id for e in future_events]
    # Only get TwoUp rows for future events
    data = TwoUp.objects.filter(event_id__in=event_ids).order_by('event_id', 'participant_name')
    # Build a mapping of event_id to event object
    events = {e.id: e for e in future_events}
    # Group rows by event_id
    grouped = defaultdict(list)
    for row in data:
        grouped[row.event_id].append(row)
    # Sort events by event_date
    sorted_events = sorted(events.values(), key=lambda e: e.event_date)
    access_token, refresh_token = generate_supabase_tokens(request.user)
    context = {
        "grouped": grouped,
        "events": events,
        "sorted_events": sorted_events,
        "SUPABASE_URL": settings.SUPABASE_URL,
        "SUPABASE_ANON_KEY": settings.SUPABASE_ANON_KEY,
        "SUPABASE_ACCESS_TOKEN": access_token,
        "SUPABASE_REFRESH_TOKEN": refresh_token,
    }
    return render(request, "tools/two_ups.html", context)

@login_required
def racing_matcher(request):
    access_token, refresh_token = generate_supabase_tokens(request.user)
    context = {
        "SUPABASE_URL": settings.SUPABASE_URL,
        "SUPABASE_ANON_KEY": settings.SUPABASE_ANON_KEY,
        "SUPABASE_ACCESS_TOKEN": access_token,
        "SUPABASE_REFRESH_TOKEN": refresh_token,
    }
    return render(request, "tools/racing_matcher.html",context)

@login_required
def willhillbb(request):
    return render(request, "tools/willhillbb.html")

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            with transaction.atomic():
                # Create Django user
                user = User.objects.create_user(username=username, email=email, password=password)
                # Create Supabase user and store UUID
                supabase_uid = create_supabase_user(email, password)
                user.supabase_uid = supabase_uid
                user.save()
            return redirect("login")
        except Exception as e:
            return render(request, "register.html", {"error": str(e)})
    return render(request, "register.html")
