import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .supabase_admin import create_supabase_user

class Tool(models.Model):
    name = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=200, blank=True)  # <-- Change from URLField to CharField

    def __str__(self):
        return self.name

class UserToolPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'tool')

    def __str__(self):
        return f"{self.user.username} - {self.tool.name}"

class TwoUp(models.Model):
    event = models.ForeignKey('betting_data.Event', db_column='event_id', on_delete=models.DO_NOTHING)
    market_id = models.UUIDField()
    market_name = models.TextField()
    participant_id = models.UUIDField()
    participant_name = models.TextField()
    back_bookmaker = models.TextField()
    back_odds = models.DecimalField(max_digits=10, decimal_places=2)
    lay_bookmaker = models.TextField()
    lay_odds = models.DecimalField(max_digits=10, decimal_places=2)
    id = models.UUIDField(primary_key=True)

    class Meta:
        db_table = 'betting_data"."two_up'  # schema"."table for PostgreSQL
        managed = False  # Don't let Django create/drop this table

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supabase_uid = models.UUIDField(null=True, blank=True, unique=True, verbose_name="Supabase UID")

    def __str__(self):
        return f"Profile for {self.user.username}"

    class Meta:
        managed = True  # This is the default, but explicit is fine

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        # Create Supabase user and store UUID
        supabase_uid = create_supabase_user(instance.email, instance.password)
        profile.supabase_uid = supabase_uid
        profile.save()
