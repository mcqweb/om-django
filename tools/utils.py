import jwt
from django.conf import settings
from datetime import datetime, timedelta

def generate_supabase_tokens(user):
    supabase_uid = str(user.profile.supabase_uid)
    now = datetime.utcnow()

    # Access token (short-lived)
    access_payload = {
        "sub": supabase_uid,
        "email": user.email,
        "aud": "authenticated",
        "role": "authenticated",
        "exp": now + timedelta(hours=1),
        "type": "access_token",
    }
    access_token = jwt.encode(access_payload, settings.SUPABASE_JWT_SECRET, algorithm="HS256")

    # Refresh token (longer-lived)
    refresh_payload = {
        "sub": supabase_uid,
        "email": user.email,
        "aud": "authenticated",
        "role": "authenticated",
        "exp": now + timedelta(days=30),
        "type": "refresh_token",
    }
    refresh_token = jwt.encode(refresh_payload, settings.SUPABASE_JWT_SECRET, algorithm="HS256")

    return access_token, refresh_token