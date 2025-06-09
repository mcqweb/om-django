from django.db import models
from django.contrib.auth.models import User

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

class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    event_date = models.DateTimeField()

    class Meta:
        db_table = 'betting_data"."events'
        managed = False

class TwoUp(models.Model):
    event = models.ForeignKey(Event, db_column='event_id', on_delete=models.DO_NOTHING)
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
