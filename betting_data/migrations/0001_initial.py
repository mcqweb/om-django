# Generated by Django 4.2.22 on 2025-06-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('event_date', models.DateTimeField()),
                ('event_type_id', models.UUIDField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': '"betting_data"."events"',
                'managed': False,
            },
        ),
    ]
