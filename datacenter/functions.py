from django.utils import timezone
from datetime import datetime


def is_visit_long(duration, minutes=60):
    one_minute = 60
    seconds = minutes * one_minute
    return duration.seconds > seconds


def get_duration(visit):
    entered = timezone.localtime(visit.entered_at)
    if not visit.leaved_at:
        now = timezone.localtime(datetime.now(timezone.utc))
        delta = now - entered
    else:
        localtime_leaved = timezone.localtime(visit.leaved_at)
        delta = localtime_leaved - entered
    return delta


def format_duration(duration):
    total_seconds = duration.seconds
    one_hour_in_seconds = 3600
    one_minute_in_seconds = 60
    hours = total_seconds // one_hour_in_seconds
    minutes = (total_seconds % one_hour_in_seconds) // one_minute_in_seconds
    seconds = total_seconds % one_minute_in_seconds
    return f'{hours}:{minutes}:{seconds}'
