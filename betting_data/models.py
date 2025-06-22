from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    event_type_id = models.UUIDField(null=True, blank=True)

    class Meta:
        db_table = '"betting_data"."events"'
        managed = False
        app_label = 'betting_data'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f"{self.name} ({self.event_date})"

class Market(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    event = models.ForeignKey('Event', db_column='event_id', on_delete=models.DO_NOTHING, related_name='markets')
    market_name = models.CharField(max_length=255)
    # ... other fields ...

    class Meta:
        db_table = '"betting_data"."markets"'
        managed = False
        app_label = 'betting_data'
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'

    def __str__(self):
        return self.market_name

class Participant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    market = models.ForeignKey('Market', db_column='market_id', on_delete=models.DO_NOTHING, related_name='participants')
    participant_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    # ... other fields ...

    class Meta:
        db_table = '"betting_data"."participants"'
        managed = False
        app_label = 'betting_data'
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'

    def __str__(self):
        return self.participant_name

class Odds(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    participant = models.ForeignKey('Participant', db_column='participant_id', null=True, blank=True, on_delete=models.DO_NOTHING)
    event = models.ForeignKey('Event', db_column='event_id', null=True, blank=True, on_delete=models.DO_NOTHING)
    market = models.ForeignKey('Market', db_column='market_id', null=True, blank=True, on_delete=models.DO_NOTHING)
    bookmaker = models.ForeignKey('Bookmaker', db_column='bookmaker_id', null=True, blank=True, on_delete=models.DO_NOTHING)
    odds = models.DecimalField(max_digits=10, decimal_places=2)
    back_lay = models.CharField(max_length=4, choices=[('back', 'Back'), ('lay', 'Lay')], null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = '"betting_data"."odds"'
        managed = False
        app_label = 'betting_data'
        verbose_name = 'Odds'
        verbose_name_plural = 'Odds'

    def __str__(self):
        return f"{self.odds} ({self.back_lay})"

class Bookmaker(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    default_back_lay = models.CharField(max_length=4, choices=[('back', 'Back'), ('lay', 'Lay')], default='back')

    class Meta:
        db_table = '"betting_data"."bookmakers"'
        managed = False
        app_label = 'betting_data'
        verbose_name = 'Bookmaker'
        verbose_name_plural = 'Bookmakers'

    def __str__(self):
        return self.name
