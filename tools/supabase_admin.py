import requests
from django.conf import settings

def create_supabase_user(email, password):
    url = f"{settings.SUPABASE_URL}/auth/v1/admin/users"
    headers = {
        "apikey": settings.SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "email": email,
        "password": password,
    }
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()["id"]  # This is the Supabase UUID

def get_supabase_user_by_email(email):
    url = f"{settings.SUPABASE_URL}/auth/v1/admin/users"
    headers = {
        "apikey": settings.SUPABASE_SERVICE_ROLE_KEY,
        "Authorization": f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}",
        "Content-Type": "application/json",
    }
    params = {"email": email}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    users = resp.json().get("users", [])
    if users:
        return users[0]["id"]  # Supabase UUID
    return None