from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from .supabase_admin import get_supabase_user_by_email
from .models import Profile

@receiver(user_logged_in)
def sync_supabase_uid(sender, request, user, **kwargs):
    profile = getattr(user, "profile", None)
    if profile and not profile.supabase_uid:
        supabase_uid = get_supabase_user_by_email(user.email)
        if supabase_uid:
            profile.supabase_uid = supabase_uid
            profile.save()