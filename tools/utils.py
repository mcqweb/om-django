import jwt
from django.conf import settings
from datetime import datetime, timedelta

def generate_supabase_jwt(user):
    supabase_uid = str(user.profile.supabase_uid)
    payload = {
        "sub": supabase_uid,
        "email": user.email,
        "aud": "authenticated",  # <-- Add this line
        "role": "authenticated",
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(payload, settings.SUPABASE_JWT_SECRET, algorithm="HS256")
    return token