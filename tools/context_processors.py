from .models import UserToolPermission

def user_tools(request):
    tools = []
    is_admin = False
    if request.user.is_authenticated:
        tools = UserToolPermission.objects.filter(user=request.user).select_related('tool')
        is_admin = request.user.groups.filter(name='admin').exists() or request.user.is_superuser
    return {'tools': tools, 'is_admin': is_admin}