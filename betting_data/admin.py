from django.contrib import admin
from .models import Event, Market, Participant, Odds, Bookmaker

class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0
    # If your Participant model is unmanaged, add:
    can_delete = False
    show_change_link = True

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Market._meta.fields]
    search_fields = ['id']  # or any searchable field
    list_filter = ['event']
    inlines = [ParticipantInline]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    search_fields = ['name']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Participant._meta.fields]
    search_fields = ['participant_name']
    list_filter = ['market']

@admin.register(Odds)
class OddsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Odds._meta.fields]
    search_fields = ['odds', 'back_lay']
    list_filter = ['back_lay', 'event', 'market', 'participant']

@admin.register(Bookmaker)
class BookmakerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bookmaker._meta.fields]
    search_fields = ['name']
