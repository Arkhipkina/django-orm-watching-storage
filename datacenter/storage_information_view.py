from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.utils import timezone
from datacenter.functions import get_duration
from datacenter.functions import format_duration

def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration = get_duration(visit)
        entered_at = localtime(visit.entered_at)
        visit_time = format_duration(duration)
        people_visit = visit.passcard

        non_closed_visits.append({
            'who_entered': people_visit,
            'entered_at': entered_at,
            'duration': visit_time,
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
